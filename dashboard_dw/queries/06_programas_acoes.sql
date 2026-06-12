WITH programas_ano AS (
    SELECT
        t.ano,
        pa.codigo_programa,
        pa.descricao_programa,
        pa.codigo_acao,
        pa.descricao_acao,
        SUM(f.valor_empenhado) AS total_empenhado,
        SUM(f.valor_liquidado) AS total_liquidado,
        SUM(f.valor_pago) AS total_pago
    FROM tce_pb_dw.fato_empenho f
    JOIN tce_pb_dw.dim_tempo t
        ON f.sk_tempo = t.sk_tempo
    JOIN tce_pb_dw.dim_programa_acao pa
        ON f.sk_programa_acao = pa.sk_programa_acao
    GROUP BY
        t.ano,
        pa.codigo_programa,
        pa.descricao_programa,
        pa.codigo_acao,
        pa.descricao_acao
),
ranked AS (
    SELECT
        programas_ano.*,
        ROW_NUMBER() OVER (
            PARTITION BY ano
            ORDER BY total_empenhado DESC
        ) AS ranking
    FROM programas_ano
)
SELECT
    ano,
    ranking,
    codigo_programa,
    descricao_programa,
    codigo_acao,
    descricao_acao,
    total_empenhado,
    total_liquidado,
    total_pago
FROM ranked
WHERE ranking <= 30
ORDER BY ano, ranking;
