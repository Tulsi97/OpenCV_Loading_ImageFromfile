# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:48:39 2018

@author: hp-u
"""

import cv2
img = cv2.imread('sleeping-baby-article.jpg')

cropped = img[300:500,400:550]
cv2.imshow("cropped",cropped)
cv2.imwrite("thumbnail.png", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()