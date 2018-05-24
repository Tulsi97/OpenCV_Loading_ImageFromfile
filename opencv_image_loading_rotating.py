# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:35:31 2018

@author: hp-u
"""

import cv2

img = cv2.imread('sleeping-baby-article.jpg')

(h,w) = img.shape[:2]
center = (w/2,h/2)

#rotate the image by 300 degrees
M = cv2.getRotationMatrix2D(center,300,1.0)
rotated = cv2.warpAffine(img,M,(w,h))

cv2.imshow('rotated-image',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()