#Este script demuestra como se usa pandas para leer un documento de excel.
#hace una limpieza de datos basica y guarda la resultante en un nuevo excel.

import pandas as pd

# Carga el archivo Excel
excel_path = r'C:\Users\user\Desktop\Negocio\Data Sobre Actividades Economicas\Actividades Economicas en Torreon.xlsx'

try:
    df = pd.read_excel(excel_path)
except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo Excel en la ruta especificada.")
    exit()

# Limpieza básica
df.dropna(inplace=True)  # Elimina las filas con valores perdidos
df = df[df['Column Name'] > 0]  # Filtra las filas basadas en una condición en una columna específica

# Guarda la información en un nuevo archivo Excel
cleaned_excel_path = r'C:\Users\user\Desktop/cleaned_file.xlsx'

try:
    df.to_excel(cleaned_excel_path, index=False)  # No incluye el índice en el archivo de salida
    print("Operación completada con éxito. El archivo limpio se ha guardado en:", cleaned_excel_path)
except PermissionError:
    print("Error: No se puede escribir en la ruta especificada. Verifique los permisos.")
except Exception as e:
    print("Error inesperado:", e)