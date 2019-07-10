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

b_2=np.ones((row*2,column*4),dtype=b.dtype)*255
g_2=np.ones((row*2,column*4),dtype=b.dtype)*255
r_2=np.ones((row*2,column*4),dtype=b.dtype)*255
im2=cv2.merge((b_2,g_2,r_2))

#resize the logo image, enlarge it by twice
im1_res=cv2.resize(im1,(2*column,2*row),interpolation = cv2.INTER_CUBIC)
#insert the images
im2[0:row*2, 0:column*2] = im1_res
im2[0:row*2,column*2:column*4]=im1_res

cv2.imwrite(r'C:\Users\tangj\Desktop\canvas_edit.png',im2)

b,g,r=cv2.split(im2)
a_channel=np.ones(b.shape,dtype=b.dtype)*255
#regarding the image with pixels like array, if the rgb value is closer to black, make the alpha channel to 0
for i in range(a_channel.shape[0]):
    for j in range(a_channel.shape[1]):
        if b[i,j]<5 and g[i,j]<5 and r[i,j]<5:
            a_channel[i,j]=0
#merge the rgba
img_bgra=cv2.merge((b,g,r,a_channel))
#write into a new image
cv2.imwrite(r'C:\Users\tangj\Desktop\canvas_edit.png',img_bgra)