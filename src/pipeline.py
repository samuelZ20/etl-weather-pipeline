import subprocess

def run_script(script_name):
    print(f"▶️ Executando {script_name}...")
    subprocess.run(["python", f"src/{script_name}.py"], check=True)
    print(f"✅ {script_name} concluído.\n")

def main():
    print("🚀 Iniciando pipeline ETL completo\n")
    run_script("extract")
    run_script("transform")
    run_script("load")
    print("🎉 Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    main()
