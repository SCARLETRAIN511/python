import numpy as np
import cv2
from PIL import Image

im=Image.open(r'C:\Users\tangj\Desktop\yeah.jpg').convert('L')
img=np.array(im).astype(np.float32)/255
row,col=img.shape[:2]
x_edge=abs(img[:,1:]-img[:,:col-1])
y_edge=abs(img[1:,:]-img[:row-1,:])
print(x_edge.shape)
print(y_edge.shape)
gradient=np.sqrt(x_edge[:-1,:]**2+y_edge[:,:-1]**2)
t=0.009
gradient[gradient<t]=0

import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.imshow(np.uint8(gradient*255),cmap='gray')
plt.subplot(1,2,2)
plt.imshow(im,cmap='gray')
plt.show()
