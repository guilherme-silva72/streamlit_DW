import plotly.express as px
import streamlit as st

from dashboard_utils import carregar_csv, configurar_pagina, tabela


configurar_pagina("Tipo De Fornecedor")
df = carregar_csv("05_tipo_fornecedor.csv")

fig = px.bar(
    df,
    x="ano",
    y="total_pago",
    color="tipo_pessoa",
    barmode="group",
    hover_data=["qtd_fornecedores", "percentual_pago_no_ano"],
)
fig.update_layout(xaxis_title="Ano", yaxis_title="Valor pago")

tabela(df)
st.plotly_chart(fig, use_container_width=True)
