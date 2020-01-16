# adding artificial noise to an image
import numpy as np 
from matplotlib import pyplot as plt 
from skimage import io, img_as_ubyte
from scipy import ndimage as nd

img = io.imread("ImageProcessing/Images/flower1.jpg",1)

# create an artificial image
# noisy = I + 0.4 * I.std() * np.random.random(I.shape)
row, col = img.shape
random_image = np.random.normal(0,0.1,(row,col))

# add img and random_img
noised_img = img + random_image
#print(img.dtype, noised_img.dtype)

plt.imsave("ImageProcessing/Images/flower_noise.jpg",noised_img)
