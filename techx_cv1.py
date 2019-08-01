import numpy
import cv2
im_edit=cv2.imread(r'C:\Users\tangj\Desktop\p1.png')
b,g,r=cv2.split(im_edit)
for i in range(b.shape[0]):
    for j in range(b.shape[1]):
        
        g[i,j]=255*(g[i,j]/255)**(1/2.2)
        b[i,j]=255*(b[i,j]/255)**(1/2.2)
        r[i,j]=255*(r[i,j]/255)**(1/2.2)
im_new=cv2.merge((b,g,r))
cv2.imwrite(r'C:\Users\tangj\Desktop\p1_edit.png',im_new)
