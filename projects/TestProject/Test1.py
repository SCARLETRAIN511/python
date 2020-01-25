import cv2
import numpy as np

img=cv2.imread('/home/jt2418/Pictures/mo.jpg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()