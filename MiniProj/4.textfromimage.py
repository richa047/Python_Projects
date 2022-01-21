import pytesseract
from PIL import Image

value = Image.open('img1.jpg')
text = pytesseract.image_to_string(value,config='')
print(text)