print("Oscar Flores Machine Learning pandas, NC 1389")

import sys
import os
import pandas as pd
import io

# Permitir importar dicc_1389.py desde la subcarpeta hermana 'datos-de-entrada-ml-1389'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-1389')))
import dicc_1389 # type: ignore

print("Oscar Flores Machine Learning pandas, NC 1389")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Oscar Flores Machine Learning pandas, NC 1389"
contenido_md.append(f"# Reporte de Análisis de Datos - Museos (Pandas)\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario cargado desde dicc_1389 a DataFrame
df = pd.DataFrame(dicc_1389.datos_museos)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de las Columnas Numéricas (Salas y Visitantes_anio)
registrar("3. Estadísticas Generales de 'Salas' y 'Visitantes_anio'", df[['Salas', 'Visitantes_anio']].describe())

# 4. Ordenar Ascendente por Salas
df_asc_salas = df.sort_values(by="Salas", ascending=True)
registrar("4. Ordenar Ascendente por Salas", df_asc_salas)

# 5. Ordenar Descendente por Visitantes por Año
df_desc_visitantes = df.sort_values(by="Visitantes_anio", ascending=False)
registrar("5. Ordenar Descendente por Visitantes por Año", df_desc_visitantes)

# 7. Guardar el archivo resultados-ml-1389.md dentro de resultados-1389
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-1389'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-1389.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Programa realizado por Oscar Flores NC = 1389")