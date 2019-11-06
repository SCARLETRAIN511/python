import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
im=Image.open(r'C:\Users\tangj\Desktop\P1.jpg').convert('L')
img=np.array(im).astype(np.float32)/255
img_edge=cv2.Canny(np.uint8(255*img),30,155)
plt.imshow(img_edge)
plt.show()