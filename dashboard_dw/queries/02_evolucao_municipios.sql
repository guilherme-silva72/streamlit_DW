SELECT
    ea.nome_municipio,
    t.ano,
    SUM(f.valor_empenhado) AS total_empenhado,
    SUM(f.valor_liquidado) AS total_liquidado,
    SUM(f.valor_pago) AS total_pago,
    SUM(f.saldo_a_pagar) AS saldo_a_pagar
FROM tce_pb_dw.fato_empenho f
JOIN tce_pb_dw.dim_tempo t
    ON f.sk_tempo = t.sk_tempo
JOIN tce_pb_dw.dim_estrutura_administrativa ea
    ON f.sk_estrutura_admin = ea.sk_estrutura_admin
GROUP BY ea.nome_municipio, t.ano
ORDER BY ea.nome_municipio, t.ano;
