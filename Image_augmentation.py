import cv2
import sys
import numpy as np
import os
from os import listdir



#this script needs to be inside the folder with images

def adjust_gamma(image, gamma=0.5):
	# from: https://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)

#input folder
folder_dir = "/home/"
for images in os.listdir(folder_dir):

  # image ending or png etc.
  if (images.endswith(".jpg")):

  # adjust blur level from 1-100 with 100 high blur
    blur_level = 1

    # Read image
    img = cv2.imread(images)

    # Apply blur to image
    blur = cv2.GaussianBlur(img, (blur_level + 1, 0), sigmaX=blur_level, sigmaY=blur_level)
    blur = cv2.GaussianBlur(blur, (0, blur_level + 1), sigmaX=blur_level, sigmaY=blur_level)

    # Increase brightness
    blur = adjust_gamma(img, 1.5)
    # if blurr is applied
    #blur = adjust_gamma(img, 1.5)

    # rewrite old image
    cv2.imwrite(images, blur)
