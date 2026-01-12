import sqlite3
import pandas as pd

#conecta ao banco SQLite
conn = sqlite3.connect("data/clima.db")
df = pd.read_sql("SELECT * FROM clima", conn)
conn.close()

#análises simples
print("Temperatura média:", df["temperatura"].mean())
print("Dias com chuva:", df["chovendo"].value_counts())
print("Condições climáticas mais comuns:")
print(df["condicao"].value_counts())
