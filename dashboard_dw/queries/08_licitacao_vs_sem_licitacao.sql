SELECT
    t.ano,
    CASE
        WHEN f.sk_licitacao = -1 THEN 'SEM LICITACAO VINCULADA'
        ELSE 'COM LICITACAO IDENTIFICADA'
    END AS situacao_licitacao,
    COUNT(*) AS qtd_grupos_fato,
    SUM(f.valor_empenhado) AS total_empenhado,
    SUM(f.valor_liquidado) AS total_liquidado,
    SUM(f.valor_pago) AS total_pago,
    SUM(f.valor_empenhado) / SUM(SUM(f.valor_empenhado)) OVER (PARTITION BY t.ano) * 100
        AS percentual_empenhado_no_ano
FROM tce_pb_dw.fato_empenho f
JOIN tce_pb_dw.dim_tempo t
    ON f.sk_tempo = t.sk_tempo
GROUP BY
    t.ano,
    situacao_licitacao
ORDER BY t.ano, total_empenhado DESC;
