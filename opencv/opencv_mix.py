from django.conf import settings
import numpy as np
import cv2


def opencv_mix(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    add_img1 = img1 + img2
    add_img2 = cv2.add(img1, img2)

    cv2.imwrite(imgfile1, add_img1)
    cv2.imwrite(imgfile2, add_img2)

        
