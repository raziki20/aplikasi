import cv2
from matplotlib import pyplot as plt


def gray(namafile):
    image = cv2.imread(namafile)
    image = cv2.resize(image,(300,300))
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("RGB", image)
    cv2.imshow("GRAY", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()