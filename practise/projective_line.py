import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
img=Image.open(r'C:\Users\tangj\Desktop\lab2.jpg').convert('L')
img=np.array(img).astype(np.float32)/255
img_edge=cv2.Canny(np.uint8(255*img),30,155)
plt.imshow(img_edge)
plt.show()