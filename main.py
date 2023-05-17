import os.path
import fitz
from PIL import Image
import pytesseract

chemin_fichier = "fichiers/nature.pdf"
fullText = ""
zoom = 3 #Zoomer image de 150%

# Fitz est une librairie qui permet de manipuler des fichiers PDF
document = fitz.Document(chemin_fichier)
matrice_zoom = fitz.Matrix(zoom, zoom)
# Nombre de pages du document PDF
nombre_de_pages = document.page_count

for numero_page in range(nombre_de_pages):
    # Récupérer la page et la convertir en image zoomée (150%)
    page = document.load_page(numero_page)
    pix = page.get_pixmap(matrix = matrice_zoom)
    output = "temp/" + str(numero_page) + ".jpg"
    pix.save(output, "jpg")
    # Tesseract est un logiciel de reconnaissance optique de caractères (OCR)
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    text = str(pytesseract.image_to_string(Image.open("temp/" + str(numero_page) + ".jpg")))
    fullText += text

# On écrit le texte dans un fichier texte
with open('outputs/nature.txt', 'w') as txt_file:
    txt_file.write(fullText)
