import sqlite3
import pandas as pd

def check_data_quality():
    conn = sqlite3.connect("data/clima.db")
    
    # carrega os dados
    query = "SELECT * FROM clima ORDER BY data_hora DESC"
    df = pd.read_sql(query, conn)
    
    print("Resumo dos Dados no Banco:")
    print(f"- Total de registros: {len(df)}")
    print(f"- Temperatura Máxima: {df['temperatura'].max()}°C")
    print(f"- Temperatura Mínima: {df['temperatura'].min()}°C")
    
    # preparação para o Dashboard
    # criar uma média móvel para suavizar o gráfico no BI
    df['media_movel_temp'] = df['temperatura'].rolling(window=3).mean()
    
    conn.close()
    return df

if __name__ == "__main__":
    check_data_quality()