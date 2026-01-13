import os
import sqlite3
import pandas as pd

DB_PATH = "data/clima.db"
CSV_PATH = "data/processed/clima_lavras.csv"
TABLE_NAME = "clima"

def main():
    print("Iniciando etapa LOAD...")
    
    if not os.path.exists(CSV_PATH):
        print(f"Abortando: Arquivo {CSV_PATH} não encontrado.")
        return

    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    try:
        #criar tabela
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                cidade TEXT, timestamp INTEGER PRIMARY KEY, data_hora TEXT,
                temperatura REAL, umidade REAL, condicao TEXT, vento REAL, chovendo INTEGER
            );
        """)

        #ler e filtrar duplicados
        df = pd.read_csv(CSV_PATH)
        
        #buscar timestamps que já existem no banco
        existentes = pd.read_sql(f"SELECT timestamp FROM {TABLE_NAME}", conn)["timestamp"].values
        df_novo = df[~df["timestamp"].isin(existentes)]

        if not df_novo.empty:
            df_novo.to_sql(TABLE_NAME, conn, if_exists="append", index=False)
            print(f"{len(df_novo)} novas linhas inseridas no SQLite.")
        else:
            print("Nenhuma novidade para inserir.")

    except Exception as e:
        print(f"Erro no Load: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()