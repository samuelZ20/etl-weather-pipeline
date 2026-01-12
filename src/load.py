import os
import sqlite3
import pandas as pd

DB_PATH = "data/clima.db"
CSV_PATH = "data/processed/clima_lavras.csv"
TABLE_NAME = "clima"

def garantir_pasta_data():
    # garante que a pasta 'data' exista para armazenar o banco
    os.makedirs("data", exist_ok=True)

def conectar_banco(db_path: str):
    # abre conexão com o SQLite; cria o arquivo se não existir
    return sqlite3.connect(db_path)

def criar_tabela_se_nao_existir(conn):
    # cria a tabela com schema compatível com o CSV
    sql = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        cidade      TEXT,
        timestamp   INTEGER PRIMARY KEY,
        data_hora   TEXT,
        temperatura REAL,
        umidade     REAL,
        condicao    TEXT,
        vento       REAL,
        chovendo    INTEGER
    );
    """
    conn.execute(sql)
    conn.commit()

def ler_csv(csv_path: str) -> pd.DataFrame:
    # lê o CSV transformado em DataFrame
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"❌ CSV não encontrado em: {csv_path}")
    df = pd.read_csv(csv_path, encoding="utf-8")
    return df

def normalizar_tipos(df: pd.DataFrame) -> pd.DataFrame:
    # ajusta tipos para compatibilidade com o banco
    df["timestamp"]   = pd.to_numeric(df["timestamp"], errors="coerce").astype("Int64")
    df["temperatura"] = pd.to_numeric(df["temperatura"], errors="coerce")
    df["umidade"]     = pd.to_numeric(df["umidade"], errors="coerce")
    df["vento"]       = pd.to_numeric(df["vento"], errors="coerce")
    df["chovendo"]    = df["chovendo"].astype(int) 
    return df

def remover_duplicatas_por_timestamp(conn, df: pd.DataFrame) -> pd.DataFrame:
    # remove linhas cujo timestamp já exista na tabela
    cursor = conn.execute(f"SELECT timestamp FROM {TABLE_NAME}")
    existentes = {row[0] for row in cursor.fetchall()}
    df_filtrado = df[~df["timestamp"].isin(existentes)].copy()
    return df_filtrado

def inserir_dataframe(conn, df: pd.DataFrame):
    # insere o DataFrame na tabela (append)
    df.to_sql(TABLE_NAME, conn, if_exists="append", index=False)

def main():
    print("🚀 Iniciando etapa LOAD")
    garantir_pasta_data()

    # Conectar ao banco
    conn = conectar_banco(DB_PATH)
    try:
        # Criar tabela se não existir
        criar_tabela_se_nao_existir(conn)

        # Ler CSV
        df = ler_csv(CSV_PATH)

        # Normalizar tipos
        df = normalizar_tipos(df)

        # Remover duplicatas por timestamp
        df = remover_duplicatas_por_timestamp(conn, df)

        if df.empty:
            print("ℹ️ Nenhuma nova linha para inserir (tudo já existe por timestamp).")
        else:
            # Inserir no banco
            inserir_dataframe(conn, df)
            print(f"✅ Inseridas {len(df)} linhas em {TABLE_NAME} no banco {DB_PATH}")

    finally:
        conn.close()
        print("🔒 Conexão com o banco encerrada.")

if __name__ == "__main__":
    main()
