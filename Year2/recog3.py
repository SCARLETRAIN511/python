import pytesseract
from PIL import Image

def main():
    filename = input('Input the name of the image inside this file')
    pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))
    print(text)

if __name__ == "__main__":
    main()