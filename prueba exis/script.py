import pandas as pd
from datetime import datetime
import numpy as np
# import yfinance as yf
import shelve
import pickle


# Parte 1

df = pd.read_csv('clientes.csv',sep = ";")
print("PARTE 1")
print(df.head(3))
print(df.describe())

mexico_df = df[df["Pais"] == "México"]
print(mexico_df)
print(df[["Nombre", "Compras"]])
print(df["Pais"].value_counts())

# Parte 2

df["Fecha_Registro"] = pd.to_datetime(df["Fecha_Registro"], errors='coerce')
filtro = (df["Edad"] > 30) & (df["Compras"] > 2)
print("PARTE 2")
print(df[filtro])

df["Promedio_Compra"] = df.apply(lambda row: row["Ingresos"]/row["Compras"] if row["Compras"] > 0 else 0, axis = 1)
df = df.sort_values(by = "Ingresos", ascending = False)
print(df.groupby("Pais")["Ingresos"].mean())  

# Parte 3

agrupado = df.groupby("Pais").agg(Numero_Clientes = ("Nombre", "count"), Total_Ingresos = ("Ingresos", "sum"), Promedio_Edad = ("Edad", "mean"))
print("PARTE 3")
print(agrupado)

hoy = pd.to_datetime(datetime.today())
# df["Dias_Desde_Registro"] = (hoy - df["Fecha_Registro"].dt.days)

tabla_pivote = df.pivot_table(
    index = "Pais",
    columns = "Genero",
    values = "Ingresos",
    aggfunc = "sum", 
    fill_value = 0
)

print(tabla_pivote)

subconjunto = df[(df["Edad"] > 30) & (df["Compras"]) > 2]
subconjunto.to_csv("Clientes_Filtrados.csv", index=False)

# Parte 4

#ticker = "0P0000TKZK.L"
#data = yf.download(ticker)
#precio_cierre = data["Close"].resample("D").mean()
#precio_cierre.to_excel("precios_cierre.xlsx")

# Parte 5
with open("datos_punto_5.pkl", "rb") as f:
          datos_p5 = pickle.load(f)

alta_cardinalidad = [col for col in datos_p5.columns if datos_p5[col].nunique() > 100]
print("Columnas alta cardinalidad", alta_cardinalidad)

resumen = pd.DataFrame({
        "nombre_columna": datos_p5.columns,
        "tipo_dato": datos_p5.dtypes,
        "valores_unicos": [datos_p5[col].isna().mean() * 100 for col in datos_p5.columns]
}
)