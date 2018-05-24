# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:27:41 2018

@author: hp-u
"""

import cv2
img = cv2.imread('cute-baby.jpg',-1)

print(img) 
print(type(img))
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()