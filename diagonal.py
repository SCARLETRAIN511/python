import cv2
import numpy as np
from PIL import Image
img=Image.new('RGB',(128,128),'white')
img.save(r'C:\Users\tangj\Desktop\diagonal.png')

im_edit=cv2.imread(r'C:\Users\tangj\Desktop\diagonal.png')
b,g,r=cv2.split(im_edit)
for i in range(b.shape[0]):
    b[i,i]=0
    g[i,i]=0
    r[i,i]=0

im2_edit=cv2.merge((r,g,b))
cv2.imwrite(r'C:\Users\tangj\Desktop\diagonal1.png',im2_edit)