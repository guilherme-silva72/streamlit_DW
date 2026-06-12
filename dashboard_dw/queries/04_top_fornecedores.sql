WITH fornecedores_ano AS (
    SELECT
        t.ano,
        fo.nome,
        fo.cpf_cnpj,
        fo.tipo_pessoa,
        SUM(f.valor_pago) AS total_pago,
        SUM(f.valor_empenhado) AS total_empenhado
    FROM tce_pb_dw.fato_empenho f
    JOIN tce_pb_dw.dim_tempo t
        ON f.sk_tempo = t.sk_tempo
    JOIN tce_pb_dw.dim_fornecedor fo
        ON f.sk_fornecedor = fo.sk_fornecedor
    GROUP BY
        t.ano,
        fo.nome,
        fo.cpf_cnpj,
        fo.tipo_pessoa
),
ranked AS (
    SELECT
        fornecedores_ano.*,
        ROW_NUMBER() OVER (
            PARTITION BY ano
            ORDER BY total_pago DESC
        ) AS ranking
    FROM fornecedores_ano
)
SELECT
    ano,
    ranking,
    nome,
    cpf_cnpj,
    tipo_pessoa,
    total_pago,
    total_empenhado
FROM ranked
WHERE ranking <= 30
ORDER BY ano, ranking;
