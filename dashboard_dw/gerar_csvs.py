import argparse
import getpass
import logging
import os
from pathlib import Path
from typing import List, Optional

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


ROOT = Path(__file__).resolve().parent
DEFAULT_QUERIES_DIR = ROOT / "queries"
DEFAULT_DATA_DIR = ROOT / "data"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def criar_engine():
    password = os.getenv("DB_PASS") or getpass.getpass("Digite a senha do banco de dados: ")
    url = URL.create(
        "mysql+pymysql",
        username=os.getenv("DB_USER", "root"),
        password=password,
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME", "tce_pb_dw"),
    )
    return create_engine(url, pool_recycle=3600)


def arquivos_sql(queries_dir: Path, selecionadas: Optional[List[str]]):
    arquivos = sorted(queries_dir.glob("*.sql"))
    if not selecionadas:
        return arquivos

    prefixos = tuple(selecionadas)
    filtrados = [arquivo for arquivo in arquivos if arquivo.stem.startswith(prefixos)]
    if not filtrados:
        raise SystemExit(f"Nenhuma query encontrada para: {', '.join(selecionadas)}")
    return filtrados


def exportar_query(engine, sql_path: Path, data_dir: Path):
    sql = sql_path.read_text(encoding="utf-8")
    output_path = data_dir / f"{sql_path.stem}.csv"

    logging.info("Executando %s", sql_path.name)
    df = pd.read_sql_query(text(sql), engine)
    df.to_csv(output_path, index=False, encoding="utf-8")
    logging.info("  %s linhas gravadas em %s", f"{len(df):,}", output_path)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Executa as queries analiticas do DW e materializa os resultados em CSV."
    )
    parser.add_argument(
        "--queries-dir",
        type=Path,
        default=DEFAULT_QUERIES_DIR,
        help="Diretorio com arquivos .sql.",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help="Diretorio de saida dos CSVs.",
    )
    parser.add_argument(
        "--query",
        action="append",
        help="Prefixo de uma query especifica para executar, ex.: --query 01 --query 05.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    args.data_dir.mkdir(parents=True, exist_ok=True)

    engine = criar_engine()
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    logging.info("Conexao com MySQL estabelecida.")

    for sql_path in arquivos_sql(args.queries_dir, args.query):
        exportar_query(engine, sql_path, args.data_dir)

    logging.info("Exportacao finalizada.")


if __name__ == "__main__":
    main()
