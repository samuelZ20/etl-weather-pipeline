from src.extract import main as extract_main
from src.transform import main as transform_main
from src.load import main as load_main

def main():
    print("--- INICIANDO PIPELINE ETL ---")
    extract_main()
    transform_main()
    load_main()
    print("--- PIPELINE FINALIZADA ---")

if __name__ == "__main__":
    main()