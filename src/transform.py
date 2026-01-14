import json
import pandas as pd
import os
from datetime import datetime

def main():
    pasta_raw = "data/raw"
    # Filtrar apenas arquivos .json e ordenar para pegar o mais recente
    arquivos = sorted([f for f in os.listdir(pasta_raw) if f.endswith('.json')])
    
    if not arquivos:
        print("⚠️ Nenhum arquivo JSON encontrado para transformar.")
        return

    arquivo_entrada = os.path.join(pasta_raw, arquivos[-1])
    print(f"🔄 Transformando o arquivo mais recente: {arquivo_entrada}")

    with open(arquivo_entrada, "r", encoding="utf-8") as f:
        dados = json.load(f)

    try:
        # 1. Extração dos dados base
        temp = dados.get("main", {}).get("temp")
        umidade = dados.get("main", {}).get("humidity")
        condicao = dados.get("weather", [{}])[0].get("description", "").lower()
        dt_raw = dados.get("dt")
        cidade = dados.get("name")
        vento = dados.get("wind", {}).get("speed")

        # 2. Lógica de Negócio Agrícola (Lavras - Foco Café)
        # Risco de Ferrugem: Umidade > 80% E Temp entre 18°C e 24°C
        risco_ferrugem = 1 if (umidade > 80 and 18 <= temp <= 24) else 0
        
        # Estresse Térmico: Café Arábica sofre acima de 30°C
        estresse_termico = 1 if temp > 30 else 0

        # 3. Criação do DataFrame com os novos indicadores
        df = pd.DataFrame([{
            "cidade": cidade,
            "timestamp": dt_raw,
            "data_hora": datetime.fromtimestamp(dt_raw).strftime("%Y-%m-%d %H:%M:%S"),
            "temperatura": temp,
            "umidade": umidade,
            "condicao": condicao,
            "vento": vento,
            "risco_ferrugem": risco_ferrugem,
            "estresse_termico": estresse_termico
        }])

        # 4. Salvamento incremental no CSV
        pasta_processed = "data/processed"
        os.makedirs(pasta_processed, exist_ok=True)
        arquivo_saida = os.path.join(pasta_processed, "clima_lavras.csv")

        # Se o arquivo não existe, cria com cabeçalho (header). Se existe, apenas adiciona (append).
        hdr = not os.path.exists(arquivo_saida)
        df.to_csv(arquivo_saida, mode="a", header=hdr, index=False, encoding="utf-8")
        
        print(f"✅ Dados transformados com sucesso em {arquivo_saida}")

    except Exception as e:
        print(f"❌ Erro ao processar campos do JSON: {e}")

if __name__ == "__main__":
    main()