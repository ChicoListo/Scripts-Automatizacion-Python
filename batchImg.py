#Este Script usa la libreria Pillow para cambiar el tamao de imagenes en una carpeta y guardarlas en una nueva carpeta.
# Este script utiliza la librería Pillow para cambiar el tamaño de imágenes en una carpeta
# y guardarlas en una nueva carpeta.

from PIL import Image
from pathlib import Path

# Rutas de las carpetas de entrada y salida
input_folder = Path('ruta/a/tu/carpeta/de/entrada')
output_folder = Path('ruta/a/tu/carpeta/de/salida')
# Tamaño deseado de las imágenes (ancho, alto)
new_size = (800, 600)

def resize_images(input_folder, output_folder, new_size):
    """
    Cambia el tamaño de todas las imágenes en una carpeta y las guarda en otra carpeta.

    Args:
    - input_folder: Carpeta de entrada de las imágenes.
    - output_folder: Carpeta de salida de las imágenes.
    - new_size: Tamaño deseado de las imágenes como una tupla (ancho, alto).
    """
    # Crear la carpeta de salida si no existe
    output_folder.mkdir(parents=True, exist_ok=True)

    # Procesar cada archivo en la carpeta de entrada
    for file in input_folder.iterdir():
        if file.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            image = Image.open(file)
            # Cambiar el tamaño de la imagen
            resized_image = image.resize(new_size)
            # Guardar la imagen en la carpeta de salida
            resized_image.save(output_folder / file.name)

if __name__ == '__main__':
    resize_images(input_folder, output_folder, new_size)
