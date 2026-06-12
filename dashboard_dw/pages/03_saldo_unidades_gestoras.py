import plotly.express as px
import streamlit as st

from dashboard_utils import carregar_csv, configurar_pagina, tabela


configurar_pagina("Saldo Por Unidade Gestora")
df = carregar_csv("03_saldo_unidades_gestoras.csv")
top_n = st.sidebar.slider("Quantidade", 10, 50, 25)
df_view = df.head(top_n)

fig = px.bar(
    df_view.sort_values("saldo_a_pagar"),
    x="saldo_a_pagar",
    y="descricao_unidade_gestora",
    color="nome_municipio",
    orientation="h",
)
fig.update_layout(xaxis_title="Saldo a pagar", yaxis_title="")

tabela(df_view)
st.plotly_chart(fig, use_container_width=True)
