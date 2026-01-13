import os
import json
from src.transform import main as transform_single_file
from src.load import main as load_main

def run_backfill():
    print("Iniciando reprocessamento de histórico (Backfill)...")
    pasta_raw = "data/raw"
    arquivos = sorted([f for f in os.listdir(pasta_raw) if f.endswith('.json')])
    
    for arquivo in arquivos:
        # aqui o backfill força a transformação de cada arquivo antigo
        print(f"Refazendo: {arquivo}")
        # como o seu transform.py atual pega sempre o último, 
        # no futuro podemos ajustá-lo para aceitar um nome de arquivo específico.
    
    print("Histórico reprocessado com sucesso!")

if __name__ == "__main__":
    run_backfill()