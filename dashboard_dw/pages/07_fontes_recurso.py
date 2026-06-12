import plotly.express as px
import streamlit as st

from dashboard_utils import carregar_csv, configurar_pagina, filtrar_ano, tabela


configurar_pagina("Fontes De Recurso")
df = filtrar_ano(carregar_csv("07_fontes_recurso.csv"))

fig = px.bar(
    df.head(30).sort_values("total_empenhado"),
    x="total_empenhado",
    y="descricao_fonte_recurso",
    color="ano",
    orientation="h",
    hover_data=["codigo_fonte_recurso", "ano_fonte", "percentual_empenhado_no_ano"],
)
fig.update_layout(xaxis_title="Valor empenhado", yaxis_title="")

tabela(df)
st.plotly_chart(fig, use_container_width=True)
