import cv2
import numpy as np

img=cv2.imread(r'C:\Users\tangj\Desktop\Q2.png')
b,g,r=cv2.split(img)
a_channel=np.ones(b.shape,dtype=b.dtype)*255
for i in range(a_channel.shape[0]):
    for j in range(a_channel.shape[1]):
        if b[i,j]<5 and g[i,j]<5 and r[i,j]<5:
            a_channel[i,j]=0
img_bgra=cv2.merge((b,g,r,a_channel))
cv2.imwrite(r'C:\Users\tangj\Desktop\Q2_edit.png',img_bgra)