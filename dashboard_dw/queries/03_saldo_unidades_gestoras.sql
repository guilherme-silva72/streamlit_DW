SELECT
    ea.nome_municipio,
    ea.codigo_unidade_gestora,
    ea.descricao_unidade_gestora,
    SUM(f.valor_empenhado) AS total_empenhado,
    SUM(f.valor_pago) AS total_pago,
    SUM(f.saldo_a_pagar) AS saldo_a_pagar
FROM tce_pb_dw.fato_empenho f
JOIN tce_pb_dw.dim_estrutura_administrativa ea
    ON f.sk_estrutura_admin = ea.sk_estrutura_admin
GROUP BY
    ea.nome_municipio,
    ea.codigo_unidade_gestora,
    ea.descricao_unidade_gestora
HAVING saldo_a_pagar > 0
ORDER BY saldo_a_pagar DESC
LIMIT 50;
