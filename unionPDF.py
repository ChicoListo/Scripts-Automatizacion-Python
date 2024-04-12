import PyPDF2
import os

def merge_pdfs(pdf_files, output_path):
    """
    Une varios archivos PDF en un solo archivo.

    Args:
        pdf_files (list of str): Lista de rutas de archivos PDF para unir.
        output_path (str): Ruta de salida para el archivo PDF unido.
    """
    # Crear una instancia de PdfFileMerger
    merger = PyPDF2.PdfFileMerger()

    # Añadir cada archivo PDF al objeto merger
    for pdf in pdf_files:
        try:
            with open(pdf, 'rb') as pdf_file:
                merger.append(pdf_file)
        except FileNotFoundError:
            print(f"El archivo {pdf} no se encontró y no será incluido en el archivo final.")
        except Exception as e:
            print(f"Error al añadir {pdf}: {e}")

    # Escribir el PDF combinado en el archivo de salida
    try:
        with open(output_path, 'wb') as f_out:
            merger.write(f_out)
        print(f"Todos los archivos PDF han sido combinados exitosamente en {output_path}")
    except Exception as e:
        print(f"Error al escribir el archivo combinado: {e}")
    finally:
        merger.close()

# Ejemplo de uso
pdf_files = ['path/to/pdf1.pdf', '/path/to/pdf2.pdf']
output_path = '/path/to/merged.pdf'
merge_pdfs(pdf_files, output_path)
