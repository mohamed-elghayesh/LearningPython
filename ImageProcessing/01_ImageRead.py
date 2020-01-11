# image handeling libraries are PIL, OpenCV, Scikit-image, Matplotlib
# pip install scikit-image
from skimage import io
from skimage.color import rgb2grey
from skimage import img_as_float, img_as_ubyte

import numpy as np
from matplotlib import pyplot as plt

# read and print an image (numpy)
my_image = io.imread("ImageProcessing/Images/blur.jpg")
#print(type(my_image))
#print(my_image)
plt.imshow(my_image)
plt.show()
print(my_image.min(), my_image.max())

# simple line 
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()

# create an artificial image
random_image = np.random.random([361,480])
#plt.plot(random_image)
#plt.show()
plt.imshow(random_image)
plt.show()

# show as grey image
plt.imshow(random_image, cmap="Greys")
plt.show()

# min and max values in the image
print("min = %.3f , max = %.3f" %(random_image.min(), random_image.max()))

# create image from a list
my_list = [[[100,20,30],[100,50,200],[230,200,150]],
            [[60,60,60],[90,90,90],[180,180,180]],
            [[0,0,255],[0,255,0],[255,0,0]]]
list_image = np.array(my_list)
plt.imshow(list_image)
plt.show()

# convert data types from uint to float
float_image = img_as_float(my_image)
print("min = %.3f , max = %.3f" %(float_image.min(), float_image.max()))
ubyte_image = img_as_ubyte(random_image)
print("min = %d , max = %d" %(ubyte_image.min(), ubyte_image.max()))

# converting my_image to grey image
grey_image = rgb2grey(my_image)
plt.imshow(grey_image)
plt.show()
print("min = %.3f , max = %.3f" %(grey_image.min(), grey_image.max()))

# gray image using lambda
gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
gray_image = gray(my_image)
plt.imshow(gray_image)
plt.show() 

# darkening my_image
dark_image = gray_image * 0.5
plt.imshow(dark_image)
plt.show()
print("min = %.3f , max = %.3f" %(dark_image.min(), dark_image.max()))

# image addition (same size 361*480)
add_result = grey_image + random_image
plt.imshow(add_result)
plt.show()

# slicing the red R component my_image[:,:,0]
# slicing the green G my_image[:,:,1]
# slicing the blue B my_image[:,:,2]
# zero_image = np.zeros(pic.shape, dtype="uint8")
zero_image = my_image * 0
red_slice = my_image[:,:,0]
zero_image[:,:,0] = red_slice
red_image = zero_image 
plt.imshow(red_image)
plt.show()

# draw colored rows
edited_image = my_image.copy()

edited_image[100:120,:,0] = 255
plt.imshow(edited_image)
plt.show()

edited_image[160:180,:,1] = 255
plt.imshow(edited_image)
plt.show()

edited_image[220:240,:,2] = 255
plt.imshow(edited_image)
plt.show()

# draw colored boxes
boxed_image = my_image.copy()
boxed_image[50:100,50:100,:] = [255,255,255] # white
boxed_image[100:150,100:150,:] = [255,255,0] # yellow
boxed_image[150:200,150:200,:] = [0,255,0] # green
plt.imshow(boxed_image)
plt.show()