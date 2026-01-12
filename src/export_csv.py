import sqlite3
import pandas as pd

conn = sqlite3.connect("data/clima.db")
df = pd.read_sql("SELECT * FROM clima", conn)
conn.close()

df.to_csv("data/processed/clima_full.csv", index=False)
print("CSV gerado com sucesso: data/processed/clima_full.csv")
