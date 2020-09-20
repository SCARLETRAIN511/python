import numpy as np
import cv2
im1=cv2.imread(r'C:\Users\tangj\Desktop\hello_world.jpeg')
b,g,r=cv2.split(im1)
print(im1.dtype)