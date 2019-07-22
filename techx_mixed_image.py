#tthis script will mix the two images together
#wrote by Jiaxuan Tang 20/07/2019
#import modules
import numpy as np
import cv2
from scipy import ndimage, misc
from PIL import Image
import matplotlib.pyplot as plt

#first read the Marilyn image and apply fourier transform on it.
im_m=cv2.imread(r'C:\Users\tangj\Desktop\marilyn.png',cv2.IMREAD_GRAYSCALE)
print(im_m.shape)
#use fourier transform
#im_1 = np.abs(np.fft.fft2(im_m))#this is the image after fourier trasnsform
im_1 = cv2.GaussianBlur(im_m, (11,11),4)
#this is the image after gussain filter
#im_1=np.abs(np.fft.ifft2(result))

#then read the Einstein image and apply fourier transform on it.
im_e=cv2.imread(r'C:\Users\tangj\Desktop\einstein.png',cv2.IMREAD_GRAYSCALE)

im_2=(im_e-cv2.GaussianBlur(im_e,(7,7),0))
#this image is after gussian filter

im_add=im_1+im_2
#now add the two images together

cv2.imwrite(r'C:\Users\tangj\Desktop\mixed.png',im_add)