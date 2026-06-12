SELECT
    t.ano,
    fo.tipo_pessoa,
    COUNT(DISTINCT fo.sk_fornecedor) AS qtd_fornecedores,
    SUM(f.valor_empenhado) AS total_empenhado,
    SUM(f.valor_liquidado) AS total_liquidado,
    SUM(f.valor_pago) AS total_pago,
    SUM(f.valor_pago) / SUM(SUM(f.valor_pago)) OVER (PARTITION BY t.ano) * 100
        AS percentual_pago_no_ano
FROM tce_pb_dw.fato_empenho f
JOIN tce_pb_dw.dim_tempo t
    ON f.sk_tempo = t.sk_tempo
JOIN tce_pb_dw.dim_fornecedor fo
    ON f.sk_fornecedor = fo.sk_fornecedor
GROUP BY t.ano, fo.tipo_pessoa
ORDER BY t.ano, total_pago DESC;
