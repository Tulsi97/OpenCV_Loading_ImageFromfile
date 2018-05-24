# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:11:06 2018

@author: hp-u
"""

import cv2

img = cv2.imread('sleeping-baby-article.jpg',-1)
cv2.line(img,(0,0),(300,300),(255,0,0),10)
cv2.rectangle(img,(100,100),(400,400),(0,255,0),5)
cv2.circle(img,(250,300),200,(0,0,255),8)

#putting a text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Cute-Baby',(0,450),font,4,(0,255,255),5,cv2.LINE_4)


cv2.imshow('Image-baby',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
