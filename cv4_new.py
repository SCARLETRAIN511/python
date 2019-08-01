#this script is to merge the two images on a blank canvas
#coded by TJX 10/07/2019
#import modules
import cv2
import numpy as np

#get the size of the opencv image
im1=cv2.imread(r'C:\Users\tangj\Desktop\Q2_edit.png')
b,g,r=cv2.split(im1)
row=b.shape[0]
column=b.shape[1]

#im1 will be the fg and im2 will be the bg
#create the canvas with white color
b_2=np.ones((row*1,column*2),dtype=b.dtype)*255
g_2=np.ones((row*1,column*2),dtype=b.dtype)*255
r_2=np.ones((row*1,column*2),dtype=b.dtype)*255
im2=cv2.merge((b_2,g_2,r_2))

#insert the images
im2[0:row, 0:column] = im1
im2[0:row,column:column*2]=im1

#get the alpha channel and eliminate the black background again
b,g,r=cv2.split(im2)
a_channel=np.ones(b.shape,dtype=b.dtype)*255
#regarding the image with pixels like array, if the rgb value is closer to black, make the alpha channel to 0
for i in range(a_channel.shape[0]):
    for j in range(a_channel.shape[1]):
        if b[i,j]<5 and g[i,j]<5 and r[i,j]<5:
            a_channel[i,j]=0
#merge the rgba
img_bgra=cv2.merge((b,g,r,a_channel))
#write into a new image called canvas_edit.png
cv2.imwrite(r'C:\Users\tangj\Desktop\canvas_edit.png',img_bgra)