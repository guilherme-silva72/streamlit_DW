import plotly.express as px
import streamlit as st

from dashboard_utils import carregar_csv, configurar_pagina, filtrar_ano, tabela


configurar_pagina("Top Fornecedores")
df = filtrar_ano(carregar_csv("04_top_fornecedores.csv"))

fig = px.bar(
    df.sort_values("total_pago"),
    x="total_pago",
    y="nome",
    color="tipo_pessoa",
    orientation="h",
    hover_data=["cpf_cnpj", "total_empenhado"],
)
fig.update_layout(xaxis_title="Valor pago", yaxis_title="")

tabela(df)
st.plotly_chart(fig, use_container_width=True)
