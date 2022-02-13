import cv2
#Read the image and stored in img object
img=cv2.imread('c:\\Users\\User\\Downloads\\exp5.jpg')


#Find width and height of image
height = img.shape[0]
print(height)
width = img.shape[1]
print(width)

#Looping to change pixel value
for x in range(height):
  for y in range(width):

     r,g,b=img[x,y]
     
     #if pixel value >200 and less than 100 then change it to 255 (maximum)
     if r>=100 and r<=200 and g>=100 and g<=200 and b>=100 and b<=200:
         
        r=255
        g=255
        b=255

     else:
         
         pass
      
     img[x,y]=r,g,b


#save sliced image
cv2.imwrite('c:\\Users\\User\\Downloads\\img_intensity_level_slicing.jpg', img)



