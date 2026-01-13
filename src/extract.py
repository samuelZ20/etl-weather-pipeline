import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

def main():
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise ValueError("API Key não encontrada no arquivo .env")
    
    cidade = "Lavras"
    url = "https://api.openweathermap.org/data/2.5/weather" 

    params = {
        "q" : cidade,
        "appid": api_key,
        "units": "metric",
        "lang": "pt_br" 
    }

    print(f"📡 Coletando dados para {cidade}...")
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() # para o código se houver erro (404, 500, etc)
        dados = response.json()

        #criar pasta se não existir
        os.makedirs("data/raw", exist_ok=True)

        #nome de arquivo sem espaços para evitar erros em sistemas diferentes
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"data/raw/clima_lavras_{timestamp}.json"

        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)

        print(f"Arquivo salvo em: {nome_arquivo}")

    except Exception as e:
        print(f"Erro na extração: {e}")

if __name__ == "__main__":
    main()