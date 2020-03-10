#this script is used to extract the black background of the picture
#coded by TJX 09/07/2019

#import the modules
import cv2
import numpy as np

img=cv2.imread(r'C:\Users\tangj\Desktop\Q2.png')
b,g,r=cv2.split(img)
a_channel=np.ones(b.shape,dtype=b.dtype)*255
#regarding the image with pixels like array, if the rgb value is closer to black, make the alpha channel to 0
for i in range(a_channel.shape[0]):
    for j in range(a_channel.shape[1]):
        if b[i,j]<5 and g[i,j]<5 and r[i,j]<5:
            a_channel[i,j]=0
#merge the rgba
img_bgra=cv2.merge((b,g,r,a_channel))
#write into a new image
cv2.imwrite(r'C:\Users\tangj\Desktop\Q2_edit.png',img_bgra)