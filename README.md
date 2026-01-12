# ETL Tempo Pipeline 🌦️

## 📌 Visão geral
Este projeto implementa um pipeline ETL (Extract, Transform, Load) para coletar dados de clima via API, transformá-los em formato tabular e carregá-los em um banco de dados SQLite/PostgreSQL.

Fluxo:
1. **Extract** → coleta dados brutos da API e salva em `data/raw`.
2. **Transform** → processa os dados brutos, cria colunas derivadas e salva CSV em `data/processed`.
3. **Load** → carrega o CSV em uma tabela `clima` no banco de dados.
4. **Pipeline** → orquestra todas as etapas em sequência.

---

## 📂 Estrutura de pastas
etl-tempo-pipeline/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── data/
│   ├── raw/          # dados brutos (JSON)
│   ├── processed/    # dados transformados (CSV)
│   └── clima.db       # banco SQLite
│
└── README.md

---

## ⚙️ Requisitos
- Python 3.10+
- Bibliotecas:
  - `requests`
  - `pandas`
  - `sqlite3` (nativo do Python)
  - `psycopg2` (se usar PostgreSQL)

Instale com:
```bash
pip install -r requirements.txt

▶️ Como rodar
Pipeline completo
bash
python src/pipeline.py
Etapas individuais
bash
python src/extract.py
python src/transform.py
python src/load.py

🗄️ Banco de dados
Tabela clima:

cidade (TEXT)

timestamp (INTEGER, chave primária)

data_hora (TEXT/DATETIME)

temperatura (REAL)

umidade (REAL)

condicao (TEXT)

vento (REAL)

chovendo (BOOLEAN/INTEGER)
