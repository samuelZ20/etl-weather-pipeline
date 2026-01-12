import sqlite3
from datetime import datetime, timedelta
import random
import os

# Caminho do banco
DB_PATH = os.path.join("data", "clima.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Intervalo de datas
start_date = datetime(2025, 12, 12)
end_date = datetime(2026, 1, 12)

# Horários por dia
horarios = ["06:00:00", "14:00:00", "22:00:00"]

# Contadores
inseridos = 0
ignorados = 0

current_date = start_date
while current_date <= end_date:
    for hora in horarios:
        dt_str = current_date.strftime("%Y-%m-%d") + " " + hora
        dt_obj = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        timestamp = int(dt_obj.timestamp())

        cursor.execute("""
            INSERT OR IGNORE INTO clima (
                cidade, timestamp, data_hora, temperatura, umidade, condicao, vento, chovendo
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            "Lavras",
            timestamp,
            dt_obj.strftime("%Y-%m-%d %H:%M:%S"),
            round(random.uniform(20, 35), 2),
            round(random.uniform(40, 80), 2),
            random.choice(["Sol", "Nublado", "Chuva"]),
            round(random.uniform(0, 15), 2),
            random.choice([0, 1])
        ))

        if cursor.rowcount == 1:
            inseridos += 1
        else:
            ignorados += 1

    current_date += timedelta(days=1)

conn.commit()

# Verificação final
cursor.execute("SELECT COUNT(*) FROM clima")
total = cursor.fetchone()[0]

cursor.execute("SELECT MIN(data_hora), MAX(data_hora) FROM clima")
min_dt, max_dt = cursor.fetchone()

conn.close()

print(f"Inseridos: {inseridos} | Ignorados (duplicatas): {ignorados}")
print(f"Total no banco: {total}")
print(f"Intervalo no banco: {min_dt} → {max_dt}")
