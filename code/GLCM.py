from importlib.resources import path
from tkinter import Image
from PIL import Image
import cv2
import sys
import os
import numpy as np
import csv
import xlsxwriter as xls   
from skimage import measure
from skimage.feature import greycomatrix, greycoprops
import math
from scipy import stats
from matplotlib import pyplot as plt

# def glcm(namafile):
#     image = cv2.imread(namafile)
#     image = cv2.resize(image,(300,300))
#     image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#     gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
#     cv2.imshow("RGB", image)
#     cv2.imshow("GRAY", gray)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

book = xls.Workbook('C:\Python38\aplikasi\data_fitur.xlsx')
sheet = book.add_worksheet()

tingkat_kematangan = ['hijau','hijau_merah','merah','merah_kuning']
sum_each_type = 50

glcm_feature = ['correlation','IDM','contrast','ASM']
angle = ['0','45','90','135']

sheet.write(0,0,'file')

column = 1

# header fitur glcm
for i in glcm_feature:
    for j in angle:
        sheet.write(0,column,i+""+j)
        column+=1
sheet.write(0,column,'Class')
column+=1
row=1

#kolom fitur
for i in tingkat_kematangan:
    for j in range(1, sum_each_type+1):
        column=0
        fullpath = os.path.join('C:\Python38\aplikasi\data_citra')
        file_name = fullpath+i+str(j)+'.jpg'
        print(file_name)
        sheet.write(row,column,file_name)
        column+=1

        # preproccessing 
        
        image = cv2.imread(file_name) 
        image = cv2.resize(image,(300,300))
        grayscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ret, image1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
        image1 = cv2.dilate(image1.copy(), None, iterations = 5)
        image1 = cv2.erode(image1.copy(), None, iterations = 5)
        g = cv2.split(image)
        segmen = [g,image1]
        dst = cv2.merge(segmen, 4)

        contours, hierarchy = cv2.findContours(image1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        select = max(contours, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(select)
        jpg = dst[y:y+h,x:x+w]

        grayscale = cv2.cvtColor(jpg, cv2.COLOR_BGR2GRAY)

        #glcm
        
        distances = [5]
        angles = [0,np.pi/4,np.pi/2,3*np.pi/4]
        levels = 256
        symetric = True
        normed = True

        glcm = greycomatrix(grayscale, distances, angles, levels, symetric, normed)
        glcm_props = [property for name in glcm_feature for propery in greycoprops(glcm, name)[0]]
        for item in glcm_props:
            sheet.write(row,column,item)
            column=1 


# def rgb2gray (rgb):
#     return np.dot(rgb[...,:3],[0.2989, 0.5870, 0.1140])

# class data:
#     def __init__(self, path):
#         img = np.array(Image.open(path))
#         self.citra = img
    
#     def insertoCsv(self, data):
#         row = data;
#         with open('data_fitur.csv', 'a') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(row)
#         csvfile.close

# import glob 
# x = 0
# tingkat_kematangan = ['hijau', 'hijau_merah', 'merah', 'merah_kuning']
# for path in tingkat_kematangan:
#     for filename in glob.glob('data_citra/'+path+'/*'):
#         data = cv2.imread(filename)
#         feature = []
#         glcm = greycomatrix(data, [1], [0, np.pi/4,np.pi/2, 3*np.pi/4], symmetric= True, normed= True)
#         correlation = greycomatrix(glcm, 'correlation')
#         idm =  greycomatrix(glcm, 'IDM')
#         contrast =  greycomatrix(glcm, 'contrast')
#         asm =  greycomatrix(glcm, 'ASM')
#         if (x < 1):
#             feature.append('cor[0][0]')
#             feature.append('cor[0][1]')
#             feature.append('cor[0][2]')
#             feature.append('cor[0][3]')

#             feature.append('idm[0][0]')
#             feature.append('idm[0][1]')
#             feature.append('idm[0][2]')
#             feature.append('idm[0][3]')

#             feature.append('con[0][0]')
#             feature.append('con[0][1]')
#             feature.append('con[0][2]')
#             feature.append('con[0][3]')

#             feature.append('asm[0][0]')
#             feature.append('asm[0][1]')
#             feature.append('asm[0][2]')
#             feature.append('asm[0][3]')
#         else :
#             feature.append(correlation[0][0])
#             feature.append(correlation[0][1])
#             feature.append(correlation[0][2])
#             feature.append(correlation[0][3])

#             feature.append(idm[0][0])
#             feature.append(idm[0][1])
#             feature.append(idm[0][2])
#             feature.append(idm[0][3])

#             feature.append(contrast[0][0])
#             feature.append(contrast[0][1])
#             feature.append(contrast[0][2])
#             feature.append(contrast[0][3])

#             feature.append(asm[0][0])
#             feature.append(asm[0][1])
#             feature.append(asm[0][2])
#             feature.append(asm[0][3])

#             feature.append(np.searchsorted(tingkat_kematangan, path))
#             data.insertoCsv(feature)
#         x=x+1
#         print (x)








