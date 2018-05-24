# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:10:07 2018

@author: hp-u
"""

import cv2

img = cv2.imread('sleeping-baby-article.jpg')

#r = 100.0/img.shape[1]
#dim = (100, int(img.shape[0]*r)) 0r
dim = (700,200)  
#dim = (wide,height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


cv2.imshow('baby_Image_resized',resized)
cv2.waitKey(0)
