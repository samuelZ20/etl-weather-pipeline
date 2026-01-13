import sys
import os

# Garante que o Python encontre a pasta 'src'
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.pipeline import main as run_pipeline
from src.analyze import check_data_quality

if __name__ == "__main__":
    print("🚀 Iniciando Execução Global do Projeto")
    
    # 1. Executa a Pipeline completa (Extract, Transform, Load)
    run_pipeline()
    
    print("\n" + "="*30)
    # 2. Executa a Análise para validar o que foi carregado
    check_data_quality()
    print("="*30)
    
    print("\n✅ Processo concluído com sucesso!")