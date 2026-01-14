import json
import pandas as pd
import os
from datetime import datetime

def main():
    pasta_raw = "data/raw"
    #filtrar apenas arquivos .json e ordenar
    arquivos = sorted([f for f in os.listdir(pasta_raw) if f.endswith('.json')])
    
    if not arquivos:
        print("Nenhum arquivo JSON encontrado para transformar.")
        return

    arquivo_entrada = os.path.join(pasta_raw, arquivos[-1])
    print(f"Transformando o arquivo mais recente: {arquivo_entrada}")

    with open(arquivo_entrada, "r", encoding="utf-8") as f:
        dados = json.load(f)

    #extração segura usando .get()
    try:
        temp = dados.get("main", {}).get("temp")
        umidade = dados.get("main", {}).get("humidity")
        condicao = dados.get("weather", [{}])[0].get("description", "").lower()
        dt_raw = dados.get("dt")

        # lógica de negócio
        # ferrugem do Café: Alta umidade (>80%) + Temperatura amena (18-24°C)
        risco_ferrugem = 1 if (umidade > 80 and 18 <= temp <= 24) else 0
        
        # estresse Térmico: Café Arábica sofre acima de 30°C
        estresse_termico = 1 if temp > 30 else 0
        df = pd.DataFrame([{
            "cidade": dados.get("name"),
            "timestamp": dados.get("dt"),
            "data_hora": datetime.fromtimestamp(dados.get("dt")).strftime("%Y-%m-%d %H:%M:%S"),
            "temperatura": dados.get("main", {}).get("temp"),
            "umidade": dados.get("main", {}).get("humidity"),
            "condicao": dados.get("weather", [{}])[0].get("description"),
            "vento": dados.get("wind", {}).get("speed"),
            "chovendo": 1 if "chuva" in dados.get("weather", [{}])[0].get("description", "").lower() else 0
        }])

        pasta_processed = "data/processed"
        os.makedirs(pasta_processed, exist_ok=True)
        arquivo_saida = os.path.join(pasta_processed, "clima_lavras.csv")

        #se existir, adiciona sem cabeçalho. Se não, cria com cabeçalho.
        hdr = not os.path.exists(arquivo_saida)
        df.to_csv(arquivo_saida, mode="a", header=hdr, index=False, encoding="utf-8")
        
        print(f"Dados transformados com sucesso em {arquivo_saida}")

    except KeyError as e:
        print(f"Erro ao processar campos do JSON: {e}")

if __name__ == "__main__":
    main()