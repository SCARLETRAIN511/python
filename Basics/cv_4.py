#this script is to merge the two images on a blank canvas
#coded by TJX 10/07/2019
#import modules
import cv2
import numpy as np
from PIL import Image
#the size of the opencv image

im1=cv2.imread(r'C:\Users\tangj\Desktop\Q2_edit.png')
b,g,r=cv2.split(im1)
row=b.shape[0]
column=b.shape[1]

#create the image of the canvas
#the canvas should be 4x wider and 2x higher than the size of the logo image
canvas=Image.new('RGB',(column*4,row*2),'white')
canvas.save(r'C:\Users\tangj\Desktop\canvas.png')
#read the created canvas image
im2=cv2.imread(r'C:\Users\tangj\Desktop\canvas.png')

#resize the logo image, enlarge it by twice
im1_res=cv2.resize(im1,(2*column,2*row),interpolation = cv2.INTER_CUBIC)
roi = im1_res[0:row*2, 0:column*2 ]

img1gray=cv2.cvtColor(im1_res,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img1gray,10,255,cv2.THRESH_BINARY)
mask_inv=cv2.bitwise_not(mask)

im2_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
im1_fg=cv2.bitwise_and(im1_res,im1_res,mask=mask)

dst = cv2.add(im2_bg,im1_fg)
im2[0:row*2, 0:column*2] = dst
im2[0:row*2,column*2:column*4]=dst


cv2.imwrite(r'C:\Users\tangj\Desktop\canvas_edit.png',im2)