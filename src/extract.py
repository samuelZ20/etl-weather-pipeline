"""
ETAPA: EXTRACT
---------------
Este script conecta na API do OpenWeather, coleta dados de clima da cidade de Lavras
e salva o JSON bruto em data/raw/ para ser usado nas próximas etapas do pipeline.

Padrão didático: comentários explicam cada passo.
"""

import requests        # biblioteca para fazer requisições HTTP
import json            # para manipular e salvar JSON
import os              # para acessar variáveis de ambiente
from dotenv import load_dotenv  # para carregar a chave da API do arquivo .env
from datetime import datetime   # para gerar nome de arquivo com data/hora


def main():
    # 1. Carregar variáveis do arquivo .env
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise ValueError("❌ API Key não encontrada. Verifique seu arquivo .env")

    # 2. Definir parâmetros da requisição
    cidade = "Lavras"
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": cidade,
        "appid": api_key,
        "units": "metric",   # Celsius
        "lang": "pt_br"      # português
    }

    # 3. Fazer a requisição
    print(f"🔄 Coletando dados de clima para {cidade}...")
    response = requests.get(url, params=params, timeout=10)

    # 4. Verificar status da resposta
    if response.status_code != 200:
        print("❌ Erro na requisição:", response.status_code, response.text)
        return

    # 5. Converter para JSON
    dados = response.json()

    # 6. Mostrar no terminal (formatado)
    print("✅ Dados recebidos:")
    print(json.dumps(dados, indent=2, ensure_ascii=False))

    # 7. Gerar nome de arquivo com timestamp
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M")
    nome_arquivo = f"data/raw/clima_lavras_{data_atual}.json"

    # 8. Salvar JSON bruto
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

    print(f"📁 Arquivo salvo em: {nome_arquivo}")


if __name__ == "__main__":
    main()