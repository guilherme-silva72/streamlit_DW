from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"


def configurar_pagina(titulo: str):
    st.set_page_config(page_title=titulo, layout="wide")
    st.title(titulo)


@st.cache_data
def carregar_csv(nome_arquivo: str) -> pd.DataFrame:
    caminho = DATA_DIR / nome_arquivo
    if not caminho.exists():
        st.error(f"Arquivo nao encontrado: {caminho}")
        st.info("Execute `python3 gerar_csvs.py` antes de abrir o dashboard.")
        st.stop()
    return pd.read_csv(caminho)


def filtrar_ano(df: pd.DataFrame):
    if "ano" not in df.columns:
        return df
    anos = sorted(df["ano"].dropna().unique())
    ano = st.sidebar.selectbox("Ano", ["Todos"] + anos)
    if ano == "Todos":
        return df
    return df[df["ano"] == ano]


def tabela(df: pd.DataFrame):
    st.dataframe(df, use_container_width=True, hide_index=True)
