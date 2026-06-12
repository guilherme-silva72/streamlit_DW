import plotly.express as px
import streamlit as st

from dashboard_utils import carregar_csv, configurar_pagina, tabela


configurar_pagina("Evolucao Por Municipio")
df = carregar_csv("02_evolucao_municipios.csv")
municipios = sorted(df["nome_municipio"].dropna().unique())
selecionados = st.sidebar.multiselect("Municipios", municipios, default=municipios[:5])
df_view = df[df["nome_municipio"].isin(selecionados)] if selecionados else df.head(0)

fig = px.line(
    df_view,
    x="ano",
    y="total_pago",
    color="nome_municipio",
    markers=True,
)
fig.update_layout(xaxis_title="Ano", yaxis_title="Valor pago")

tabela(df_view)
st.plotly_chart(fig, use_container_width=True)
