SELECT
    t.ano,
    fr.codigo_fonte_recurso,
    fr.descricao_fonte_recurso,
    fr.ano_fonte,
    SUM(f.valor_empenhado) AS total_empenhado,
    SUM(f.valor_pago) AS total_pago,
    SUM(f.valor_empenhado) / SUM(SUM(f.valor_empenhado)) OVER (PARTITION BY t.ano) * 100
        AS percentual_empenhado_no_ano
FROM tce_pb_dw.fato_empenho f
JOIN tce_pb_dw.dim_tempo t
    ON f.sk_tempo = t.sk_tempo
JOIN tce_pb_dw.dim_fonte_recurso fr
    ON f.sk_fonte_recurso = fr.sk_fonte_recurso
GROUP BY
    t.ano,
    fr.codigo_fonte_recurso,
    fr.descricao_fonte_recurso,
    fr.ano_fonte
ORDER BY t.ano, total_empenhado DESC;
