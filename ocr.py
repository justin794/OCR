import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'

Img = Image.open("c4.jpeg")

txt = pytesseract.image_to_string(Img)
print(txt)