import pandas as pd

def convert_csv_to_excel(csv_path, output_path):
    """
    Convierte un archivo CSV en un archivo Excel.

    Args:
        csv_path (str): La ruta del archivo CSV de entrada.
        output_path (str): La ruta del archivo Excel de salida.
    """
    try:
        # Leer el archivo CSV
        df = pd.read_csv(csv_path)

        # Escribir en el archivo Excel sin incluir el índice
        df.to_excel(output_path, index=False)
        
        print("El archivo CSV se ha convertido exitosamente a Excel.")
    except Exception as e:
        print("Ha ocurrido un error al convertir el archivo CSV a Excel:", str(e))

# Ejemplo de uso
convert_csv_to_excel('/path/to/input/file.csv', '/path/to/output/file.xlsx')
