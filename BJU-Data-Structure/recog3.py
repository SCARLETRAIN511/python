import pytesseract
from PIL import Image
import cv2

def main():
    cap = cv2.VideoCapture(0)
    print("摄像头是否已经打开 ？ {}".format(cap.isOpened()))

    while cap.isOpened():
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
        text = pytesseract.image_to_string(gray)
        cv2.imshow('frame',gray)
        print(text)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()