from SimpleCV.base import *
from SimpleCV.Camera import *
from SimpleCV.Color import *
from SimpleCV.Display import *
from SimpleCV.Features import *
from SimpleCV.ImageClass import *
from SimpleCV.Stream import *
from SimpleCV.Font import *
from SimpleCV.ColorModel import *
from SimpleCV.DrawingLayer import *
from SimpleCV.Segmentation import *
from SimpleCV.MachineLearning import *

#get the image
img = Image("image.png")
#use the haar algorithm
faces = img.findHaarFeatures("face.xml")
''' faces now has the locations where faces were detected. for information on how this method works, please view the README.md file in this directory '''
#print locations
for f in faces:
	print "I found a face at " + str(f.coordinates())
	#draw box around faces
	img.dl().centeredRectangle(f.coordinates(), (200,200), color=Color.BLUE)
#show image
img.show()
raw_input()
