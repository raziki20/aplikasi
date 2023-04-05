import cv2
from matplotlib import pyplot as plt
import numpy as np


def biner(namafile):
    image = cv2.imread(namafile)
    image = cv2.resize(image,(0,0), fx=0.3, fy=0.3)
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    tr,biner = cv2.threshold(gray, 90,255,cv2.THRESH_BINARY)  
    # cv2.imshow("RGB", image)
    # cv2.imshow("GRAY", gray)
    cv2.imshow("BINER", biner)
    cv2.waitKey(0)
    cv2.destroyAllWindows()