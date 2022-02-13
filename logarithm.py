import cv2
import math
import numpy as np

#Read the image and stored in img object
img=cv2.imread('c:\\Users\\User\\Downloads\\exp5.jpg')


#Find width and height of image
height = img.shape[0]
print(height)
width = img.shape[1]
print(width)

#convert image to array
img_to_array = np.asarray(img)  

#convert array to flat array
img_to_flatarray=img_to_array.flatten() 

#Finding c
c = 255 / np.log(1 + np.amax(img_to_flatarray))+1

#FIND LOG Transformation

#Looping to change pixel value
for x in range(height):
  for y in range(width):

     red,green,blue=img[x,y]
     
     #find log of pixel value
     red=c*math.log(1+red,10)
     green=c*math.log(1+green,10)
     blue=c*math.log(1+blue,10)
   
      #written modified pixel value
     img[x,y]=red,green,blue

#save logarithmic image
cv2.imwrite('c:\\Users\\User\\Downloads\\img_logarithmic.jpg', img)
