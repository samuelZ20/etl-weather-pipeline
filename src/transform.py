import json
import pandas as pd
import os
from datetime import datetime

def main():
    pasta_raw = "data/raw"
    arquivos = sorted(os.listdir(pasta_raw))
    if not arquivos:
        raise FileNotFoundError("❌ Nenhum arquivo encontrado em data/raw")
    arquivo_entrada = os.path.join(pasta_raw, arquivos[-1])  # pega o mais recente
    print(f"🔄 Lendo arquivo: {arquivo_entrada}")

    #ler o JSON
    with open(arquivo_entrada, "r", encoding="utf-8") as f:
        dados = json.load(f)

    #extrair campos importantes
    cidade = dados.get("name")
    timestamp = dados.get("dt")
    temp = dados.get("main", {}).get("temp")
    umidade = dados.get("main", {}).get("humidity")
    condicao = dados.get("weather", [{}])[0].get("description")
    vento = dados.get("wind", {}).get("speed")

    #criar colunas derivadas
    chovendo = condicao and "chuva" in condicao.lower()
    data_hora = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    #organizar em DataFrame
    df = pd.DataFrame([{
        "cidade": cidade,
        "timestamp": timestamp,
        "data_hora": data_hora,
        "temperatura": temp,
        "umidade": umidade,
        "condicao": condicao,
        "vento": vento,
        "chovendo": chovendo
    }])

    #salvar em CSV
    pasta_processed = "data/processed"
    os.makedirs(pasta_processed, exist_ok=True)
    arquivo_saida = os.path.join(pasta_processed, "clima_lavras.csv")

    #se já existir, adiciona linha; senão, cria novo
    if os.path.exists(arquivo_saida):
        df.to_csv(arquivo_saida, mode="a", header=False, index=False, encoding="utf-8")
    else:
        df.to_csv(arquivo_saida, index=False, encoding="utf-8")

    print(f"✅ Dados transformados e salvos em {arquivo_saida}")


if __name__ == "__main__":
    main()