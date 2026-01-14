import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_december_data():
    print("📅 Gerando dados históricos de Dezembro para Lavras (Padrão PT-BR)...")
    
    dados_historicos = []
    # Período de Dezembro
    data_atual = datetime(2025, 12, 1, 10, 0, 0)
    data_fim = datetime(2025, 12, 31, 22, 0, 0)
    
    # Horários da sua automação
    horarios = [10, 14, 22]

    while data_atual <= data_fim:
        if data_atual.hour in horarios:
            # Simulação de clima (Verão em Lavras)
            temp_valor = round(random.uniform(19.0, 31.0), 2)
            umidade = random.randint(60, 95)
            
            # --- TRATAMENTO PARA O POWER BI BRASILEIRO ---
            # Transforma o ponto em vírgula e garante 2 casas decimais
            # Ex: 24.0 vira "24,00" | 19.3 vira "19,30"
            temp_pt_br = "{:.2f}".format(temp_valor).replace('.', ',')
            
            # Lógica Agroclimática
            risco_ferrugem = 1 if (umidade > 80 and 18 <= temp_valor <= 24) else 0
            estresse_termico = 1 if temp_valor > 30 else 0
            
            dados_historicos.append({
                "cidade": "Lavras",
                "timestamp": int(data_atual.timestamp()),
                "data_hora": data_atual.strftime("%Y-%m-%d %H:%M:%S"),
                "temperatura": temp_pt_br, # Salvando como texto formatado para o BI
                "umidade": umidade,
                "condicao": "nublado" if umidade > 80 else "céu limpo",
                "vento": round(random.uniform(5, 15), 2),
                "risco_ferrugem": risco_ferrugem,
                "estresse_termico": estresse_termico
            })
        
        data_atual += timedelta(hours=1)

    df_final = pd.DataFrame(dados_historicos)
    
    # Garantir que a pasta existe
    os.makedirs("data/processed", exist_ok=True)
    caminho_csv = "data/processed/clima_lavras.csv"
    
    # Salva o CSV usando ponto-e-vírgula como separador (padrão brasileiro de CSV)
    # ou mantém vírgula, mas como a temperatura agora tem sua própria vírgula interna,
    # o ideal é usar o encoding 'utf-8-sig' para o Excel/Power BI abrir sem erro.
    df_final.to_csv(caminho_csv, index=False, encoding="utf-8-sig")
    
    print(f"✅ Sucesso! {len(df_final)} registros de dezembro gerados.")
    print(f"📍 Arquivo salvo em: {caminho_csv}")

if __name__ == "__main__":
    generate_december_data()