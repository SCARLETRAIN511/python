import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\tangj\Desktop\q3.png', 0) #直接读为灰度图像
f = np.fft.fft2(img)            #做频率变换
fshift = np.fft.fftshift(f)     #转移像素做幅度普

s1 = np.log(np.abs(fshift))#取绝对值：将复数变化成实数取对数的目的为了将数据变化到0-255
plt.subplot(131)
plt.imshow(img, 'gray')
plt.title('original')

plt.subplot(132)
plt.imshow(s1,'gray')
plt.title('center')

plt.show()
