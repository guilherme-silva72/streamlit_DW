import plotly.express as px
import streamlit as st

from dashboard_utils import carregar_csv, configurar_pagina, filtrar_ano, tabela


configurar_pagina("Programas E Acoes")
df = filtrar_ano(carregar_csv("06_programas_acoes.csv"))
df["programa_acao"] = (
    df["codigo_programa"].astype(str)
    + " / "
    + df["codigo_acao"].astype(str)
)

fig = px.bar(
    df.sort_values("total_empenhado"),
    x="total_empenhado",
    y="programa_acao",
    color="ano",
    orientation="h",
    hover_data=["descricao_programa", "descricao_acao", "total_pago"],
)
fig.update_layout(xaxis_title="Valor empenhado", yaxis_title="")

tabela(df)
st.plotly_chart(fig, use_container_width=True)
