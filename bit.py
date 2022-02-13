import numpy as np
from skimage import io

#Reading image and storing in img_obj object
img_obj = io.imread("c:\\Users\\User\\Downloads\\exp5.jpg",0)

# bit extraction

# img_copied have a copy of our orginal image
img_copied = img_obj.copy()

#take the row and column from shape method
row = img_obj.shape[0]
col=img_obj.shape[1]


for each_bit in range(8):
    
    #We make empty array of zeros of image height and width
    bit_map = np.zeros(img_obj.shape, dtype = np.uint8)
    
    for i in range(row):
        for j in range(col):
            
            #for each pixel we find all the bit values
            
            #by mod 2 we  get the LSB of the pixel value
            bit_map[i, j] = 255*( img_copied[i, j]%2)
            
            # WE now to right shift by divide by 2 so we can again find the LSB
            img_copied[i, j] = img_copied[i, j]/2
   
    #save 8 images (changing names) 
    io.imsave(str(each_bit)+"_Bit.jpg", bit_map)    
    