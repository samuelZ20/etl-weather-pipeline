# 🌦️ Pipeline ETL: Monitoramento Climático de Lavras-MG

Este projeto implementa uma pipeline de dados completa (ETL) para coletar, transformar e armazenar dados meteorológicos em tempo real da cidade de Lavras, Minas Gerais, utilizando a API da OpenWeather.

---

## 🚀 Sobre o Projeto
O objetivo deste projeto é demonstrar as capacidades de um Engenheiro de Dados em construir uma infraestrutura local robusta, garantindo a integridade dos dados, idempotência e prontidão para análise (Business Intelligence).

### 🎯 Perguntas de Negócio Resolvidas:
- Qual a variação térmica diária em Lavras?
- Existe correlação entre umidade e probabilidade de chuva na região?
- Qual o status climático mais frequente (Céu limpo, nublado, chuva)?

---

## 🛠️ Arquitetura Técnica

A pipeline segue o modelo modular de engenharia de dados:

1.  **Extract (`extract.py`)**: Consumo da API OpenWeather via `requests`, salvando os dados brutos em formato JSON na camada **Raw**.
2.  **Transform (`transform.py`)**: Limpeza de dados com `Pandas`, conversão de unidades (Kelvin para Celsius), tratamento de fuso horário e criação de flags de negócio.
3.  **Load (`load.py`)**: Carga dos dados processados em um banco de dados **SQLite**, com lógica de desduplicação por timestamp.
4.  **Orquestração (`run_etl.py`)**: Script mestre que gerencia a execução de todo o fluxo.



---

## 📁 Estrutura de Pastas
```text
ETL-TEMPO-PIPELINE/
├── data/
│   ├── raw/          # Dados brutos (JSON) - Camada Bronze
│   ├── processed/    # Dados limpos (CSV) - Camada Silver
│   └── clima.db      # Data Warehouse local (SQLite) - Camada Gold
├── src/              # Código fonte
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   ├── analyze.py    # Validação e métricas rápidas
│   └── backfill.py   # Reprocessamento de histórico
├── .env              # Variáveis de ambiente (Chaves de API)
├── requirements.txt  # Dependências do projeto
└── run_etl.py        # Ponto de entrada oficial
