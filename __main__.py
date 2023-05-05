######################################################
#
#Fernando Reyna Ramos
#Subject: Computer Vision
#Deadline: December 8th, 2021
#Title: 3rd Partial Evaluation - Object Detector using DNN
#
#Adapted from this tutorials:
#	Create the video: https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/
#	Object Detector using DNN and MSCOCO dataset: https://learnopencv.com/deep-learning-with-opencvs-dnn-module-a-definitive-guide/
#######################################################


################################ Set main path and folders #########################
from importlib import reload
from __main__ import *

#main_path ='C:/Users/Bullpen/Desktop/Detector de Objetos/'
main_path ='../ObjectDetector_3rdEvaluation/'

#list_inputs = ['example1', 'Taskmaster1', 'ManyPeople','Taskmaster2']
list_inputs =['Objects', 'ManyPeople']

################################ loop for all folders ##############################
for folder in list_inputs:
	print(folder)
	input_path = main_path + 'inputs/' + folder + '/'
	name_video = '_'+ folder

	# Checks if the folder ManyPeople is selected, and if it is, the type of file is changed
	if (folder == 'ManyPeople' or folder == 'Taskmaster2'):
		type_of_image = '*.jpg'
	else:
		type_of_image = '*.PNG'

	# Reload python scripts, checks if it has already been imported
	if 'create_video_from_images' in dir(): 
   		reload(create_video_from_images)
	else:
		import create_video_from_images

	if 'Detector_MSCOCO_video' in dir(): 
		reload(Detector_MSCOCO_video)
	else:
		import Detector_MSCOCO_video
