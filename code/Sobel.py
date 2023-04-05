from scipy import ndimage
import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread("1.jpeg")
image = cv2.resize(image,(0,0), fx=0.3, fy=0.3)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
tr,biner = cv2.threshold(gray, 95,255,cv2.THRESH_BINARY)       
# Matrix Sobel
sx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

sobelx = cv2.filter2D(biner, -1, sx)
sobely = cv2.filter2D(biner, -1, sy)
sobel = sobelx + sobely

cv2.imshow('sobel',sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()

