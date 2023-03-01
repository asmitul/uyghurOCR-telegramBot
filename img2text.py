from PIL import Image

import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
# print(pytesseract.image_to_string(Image.open('test.png')))
# print(pytesseract.image_to_string(Image.open('./tests/data/test.jpg')))
string = pytesseract.image_to_string(
    Image.open('test_ug.png'), lang='ukij')


print(string)

with open('test_ug.txt', 'w', encoding="utf-8") as f:
    f.write(string)
