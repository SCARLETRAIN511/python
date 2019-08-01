#this script is to modify the alpha channel of the transparent image
#coded by TJX 09/07/2019
#import modules
import cv2
import numpy as np
img=cv2.imread(r'C:\Users\tangj\Desktop\p1.png')
b,g,r=cv2.split(img)
print(b.dtype)
a_channel=np.ones(b.shape,dtype=b.dtype)*255
a_channel[:,:]=255
img_bgra=cv2.merge((b,g,r,a_channel))
cv2.imwrite(r'C:\Users\tangj\Desktop\Q2.png',img_bgra)