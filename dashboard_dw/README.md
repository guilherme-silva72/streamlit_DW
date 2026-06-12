# Dashboard DW TCE-PB

Fluxo:

```text
MySQL/tce_pb_dw -> gerar_csvs.py -> data/*.csv -> Streamlit
```

## Gerar CSVs

```bash
cd dashboard_dw
DB_USER=root DB_HOST=localhost DB_PASS='gui' python3 gerar_csvs.py
```

Para executar apenas uma consulta:

```bash
DB_USER=root DB_HOST=localhost DB_PASS='gui' python3 gerar_csvs.py --query 01
```

## Rodar Dashboard

```bash
streamlit run streamlit_app.py
```
