import streamlit as st


st.set_page_config(page_title="DW TCE-PB", layout="wide")

st.title("Dashboard DW TCE-PB")
st.write(
    "Use o menu lateral para navegar pelas oito analises. "
    "Os graficos usam apenas os CSVs gerados por `gerar_csvs.py`."
)

st.code("DB_USER=root DB_HOST=localhost DB_PASS='gui' python3 gerar_csvs.py")
st.code("streamlit run streamlit_app.py")
