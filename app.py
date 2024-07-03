import os
import shutil

# Ruta del directorio donde están los archivos
ruta_origen = 'C:/Users/willi/Downloads'

# Lista de extensiones de archivo para clasificar
extensiones = ['.jpg', '.png', '.pdf', '.txt', '.docx', '.pptx', '.jpeg', '.exe', '.JPG']

for ext in extensiones:
    # Crea una carpeta para cada tipo de archivo si no existe
    ruta_destino = os.path.join(ruta_origen, ext[1:].upper())
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)

    # Mueve los archivos al directorio correspondiente
    for archivo in os.listdir(ruta_origen):
        if archivo.endswith(ext):
            shutil.move(os.path.join(ruta_origen, archivo), os.path.join(ruta_destino, archivo))
