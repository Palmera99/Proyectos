from docx2pdf import convert
import os


def convertir_word_a_pdf(ruta_directorio):
    for archivo in os.listdir(ruta_directorio):
        if archivo.endswith(".docx"):  # Verifica si el archivo es un documento Word
            # Genera el nombre del archivo PDF reemplazando la extensión .docx con .pdf
            nuevo_nombre = archivo.replace(".docx", ".pdf")

            # Ruta completa al archivo de entrada (documento Word)
            ruta_entrada = os.path.join(ruta_directorio, archivo)

            # Ruta completa al archivo de salida (PDF)
            ruta_salida = os.path.join(ruta_directorio, nuevo_nombre)

            # Convierte el documento Word a PDF
            convert(ruta_entrada, ruta_salida)

            print(f"Archivo convertido: {archivo} -> {nuevo_nombre}")


def convertir_jpeg_a_jpg(ruta_directorio):
    # Verifica cada archivo en el directorio proporcionado
    for archivo in os.listdir(ruta_directorio):
        if archivo.endswith(".jpeg"):  # Verifica si el archivo tiene extensión .jpeg
            # Genera el nuevo nombre de archivo reemplazando .jpeg con .jpg
            nuevo_nombre = archivo.replace(".jpeg", ".jpg")

            # Renombra el archivo
            os.rename(os.path.join(ruta_directorio, archivo),
                      os.path.join(ruta_directorio, nuevo_nombre))
            print(f"Archivo convertido: {archivo} -> {nuevo_nombre}")


def renombrar_imagenes(ruta_directorio):
    contador = 1
    for archivo in os.listdir(ruta_directorio):
        if archivo.endswith(".jpg") or archivo.endswith(".jpeg"):
            # Genera el nuevo nombre de archivo con el formato "imageX.jpg"
            nuevo_nombre = f"image{contador}.jpg"

            # Renombra el archivo
            os.rename(os.path.join(ruta_directorio, archivo),
                      os.path.join(ruta_directorio, nuevo_nombre))
            print(f"Archivo renombrado: {archivo} -> {nuevo_nombre}")
            contador += 1

# Ruta al directorio que contiene los archivos de imagen


# Ruta al directorio que contiene los archivos JPEG a convertir
# Ruta al directorio que contiene los archivos Word a convertir
ruta = "C:/Users/hecto/Downloads/word_documents"
convertir_word_a_pdf(ruta)
