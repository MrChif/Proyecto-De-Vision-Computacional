#Fernando Reyna Ramos
#Subject: Computer Vision
#Deadline: December 8th, 2021
#Title: 3rd Partial Evaluation - Object Detector using DNN
#Based on: https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/

import cv2
import numpy as np
import glob
from __main__ import *

################ Obtain all the images and puts them in a list #########################
img_array = []
for filename in glob.glob(input_path + type_of_image):
    img = cv2.imread(filename)
    #cv2.imshow("image",img)
    #cv2.waitKey(0)
    height,width,layers=img.shape
    img = cv2.resize(img, (500,500))
    img_array.append(img)

################## Creates video from the list of images ###############################
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(input_path + 'test'+ name_video + '.mp4',fourcc, 1, (500,500))
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

 

