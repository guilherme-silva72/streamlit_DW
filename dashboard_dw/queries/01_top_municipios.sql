WITH municipios_ano AS (
    SELECT
        t.ano,
        ea.nome_municipio,
        SUM(f.valor_empenhado) AS total_empenhado,
        SUM(f.valor_pago) AS total_pago,
        SUM(f.saldo_a_pagar) AS saldo_a_pagar
    FROM tce_pb_dw.fato_empenho f
    JOIN tce_pb_dw.dim_tempo t
        ON f.sk_tempo = t.sk_tempo
    JOIN tce_pb_dw.dim_estrutura_administrativa ea
        ON f.sk_estrutura_admin = ea.sk_estrutura_admin
    GROUP BY t.ano, ea.nome_municipio
),
ranked AS (
    SELECT
        municipios_ano.*,
        ROW_NUMBER() OVER (
            PARTITION BY ano
            ORDER BY total_empenhado DESC
        ) AS ranking
    FROM municipios_ano
)
SELECT
    ano,
    ranking,
    nome_municipio,
    total_empenhado,
    total_pago,
    saldo_a_pagar
FROM ranked
WHERE ranking <= 20
ORDER BY ano, ranking;
