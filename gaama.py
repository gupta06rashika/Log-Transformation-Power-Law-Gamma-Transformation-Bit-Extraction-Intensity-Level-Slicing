import cv2

#Read the image and stored in img object
img=cv2.imread('c:\\Users\\User\\Downloads\\exp5.jpg')


#Find width and height of image
height = img.shape[0]
print(height)
width = img.shape[1]
print(width)

#FIND GAMMA Transformation

#Looping to change pixel value
for x in range(height):
  for y in range(width):

     red,green,blue=img[x,y]
     
     #c=1 And Gamma=0.4
     red=1*(red**0.4)
     green=1*(green**0.4)
     blue=1*(blue**0.4)
   
      #written modified pixel value
     img[x,y]=red,green,blue

#save image after gamma transformation
cv2.imwrite('c:\\Users\\User\\Downloads\\img_gamma_c_1.jpg', img)
