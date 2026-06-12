import plotly.express as px
import streamlit as st

from dashboard_utils import carregar_csv, configurar_pagina, filtrar_ano, tabela


configurar_pagina("Top Municipios")
df = filtrar_ano(carregar_csv("01_top_municipios.csv"))

fig = px.bar(
    df,
    x="nome_municipio",
    y="total_empenhado",
    color="ano",
    hover_data=["total_pago", "saldo_a_pagar"],
)
fig.update_layout(xaxis_title="", yaxis_title="Valor empenhado")

tabela(df)
st.plotly_chart(fig, use_container_width=True)
