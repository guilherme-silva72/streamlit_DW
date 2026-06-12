import plotly.express as px
import streamlit as st

from dashboard_utils import carregar_csv, configurar_pagina, tabela


configurar_pagina("Licitacao Identificada")
df = carregar_csv("08_licitacao_vs_sem_licitacao.csv")

fig = px.bar(
    df,
    x="ano",
    y="total_empenhado",
    color="situacao_licitacao",
    barmode="group",
    hover_data=["qtd_grupos_fato", "percentual_empenhado_no_ano"],
)
fig.update_layout(xaxis_title="Ano", yaxis_title="Valor empenhado")

tabela(df)
st.plotly_chart(fig, use_container_width=True)
