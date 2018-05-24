# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:31:40 2018

@author: hp-u
"""

import cv2

img = cv2.imread('sleeping-baby-article.jpg')
img = cv2.circle(img,(300,300),(300),(255,0,0))

cv2.imshow('baby_Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()