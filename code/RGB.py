from turtle import width
import cv2
import numpy as np
from matplotlib import pyplot as plt


def rgb(namafile):
    image = cv2.imread(namafile)
    image = cv2.resize(image,(300,300))
    
    blue = image[:,:,0]
    green = image[:,:,1]
    red = image[:,:,2]
    # b=np.average(blue)
    # g=np.average(green)
    # r=np.average(red)
    print(blue)
    print(green)
    print(red)
    blue, green, red = cv2.split(image)
    cv2.imshow("Blue Pixels", blue)
    cv2.imshow("Green Pixels", green)
    cv2.imshow("Red Pixels", red)
    cv2.waitKey(0)
    cv2.destroyAllWindows()