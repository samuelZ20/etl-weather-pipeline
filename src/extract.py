import requests
import json
import os #acessar variaveis do ambiente
from dotenv import load_dotenv #acessar API do .env
from datetime import datetime #salvar arquivo com data e hora atual

def main():
    #carregar a chave API do arquivo env
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise ValueError("API Key não encontrada. Verifique seu arquivo .env")
    
    cidade = "Lavras"
    url = "https://api.openweathermap.org/data/3.0/weather"

    #montando a requisição
    params = {
        "q" : cidade,
        "appid": api_key,
        "units": "metric",
        "long":"pt_br"
    }

    print(f"Coletando dados de clima para {cidade}...")
    response = requests.get(url,params=params,timeout=10)

    #validando a resposta
    if response.status_code !=200:
        print("Erro na requisição: ", response.status_code, response.text)

    #converte para JSON
    dados = response.json()

    print("Dados recebidos")
    print(json.dumps(dados,indent=2,ensure_ascii=False)) #formata bonito, com quebra de linhas

    #salvar o json com timestamp
    data_atual = datetime.now().strftime("%Y- %m- %d_%H-%M")
    nome_arquivo = f"data/raw/clima_lavras_{data_atual}.json"        


    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados,f,indent=2,ensure_ascii=False)

    print(f"Arquivo salvo em: {nome_arquivo}")

#se importar esse arquivo em outro projeto, não roda automaticamente

if __name__ == "__main__":
    main()