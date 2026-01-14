import sqlite3
import pandas as pd

def check_data_quality():
    conn = sqlite3.connect("data/clima.db")
    
    # 1. Carrega os dados ordenados pelo tempo
    query = "SELECT * FROM clima ORDER BY data_hora DESC"
    df = pd.read_sql(query, conn)
    
    if df.empty:
        print("⚠️ O banco de dados está vazio. Rode o pipeline primeiro!")
        conn.close()
        return None

    print("\n--- 📊 Relatório de Qualidade de Dados (Foco Agro) ---")
    print(f"✅ Total de registros coletados: {len(df)}")
    
    # 2. Análise de Extremos
    print(f"🌡️ Amplitude Térmica: {df['temperatura'].min()}°C a {df['temperatura'].max()}°C")
    print(f"💧 Umidade Média: {df['umidade'].mean():.2f}%")

    # 3. Validação dos Indicadores de Negócio (Café)
    total_ferrugem = df['risco_ferrugem'].sum()
    total_estresse = df['estresse_termico'].sum()
    
    print(f"🚨 Alertas de Risco de Ferrugem: {total_ferrugem}")
    print(f"🔥 Eventos de Estresse Térmico (>30°C): {total_estresse}")

    # 4. Preparação de Média Móvel (Suavização para o Dashboard)
    df['media_movel_temp'] = df['temperatura'].rolling(window=3).mean()
    
    conn.close()
    return df

if __name__ == "__main__":
    check_data_quality()