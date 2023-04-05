import cv2
import numpy as np 
import xlsxwriter as xls
from skimage.feature import greycomatrix, greycoprops
import math
from scipy import stats

book = xls.Workbook('data_fitur.xlsx')
sheet = book.add_worksheet()
sheet.write(0,0,'file')

column = 1
#kolom fitur bentuk
shape_feature = ['eccentricity','metric']
for i in shape_feature:
    sheet.write(0,column,i)
    column+-1