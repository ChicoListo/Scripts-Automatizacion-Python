#este script organiza tus archivos en la carpeta designada por tipo de archivo en carpetas

import os
import shutil

def organize_files(downloads_path, organize_dict):
    organized_files = False
    for filename in os.listdir(downloads_path):
        if os.path.isfile(os.path.join(downloads_path, filename)):
            file_ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in organize_dict.items():
                if file_ext in extensions:
                    folder_path = os.path.join(downloads_path, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(os.path.join(downloads_path, filename), folder_path)
                    organized_files = True
                    break
    if organized_files:
        print("Los archivos han sido organizados correctamente.")
    else:
        print("No se encontraron archivos para organizar.")

if __name__ == "__main__":
    downloads_path = r"F:\Descargas"  # Ruta de la carpeta de descargas
    organize_dict = {
        "Documents": ['.pdf', '.docx', '.txt'],
        "Images": ['.jpg', '.jpeg', '.png', '.gif'],
        "Videos": ['.mp4', '.mov', '.avi'],
    }
    organize_files(downloads_path, organize_dict)