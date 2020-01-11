# pip install scikit-image
from skimage import io, img_as_float, img_as_ubyte
import matplotlib.pyplot as plt

img = io.imread("ImageProcessing/Images/blur.jpg")
print(type(img)) # numpy ndarray
print(img.shape) # tuple of (width,height,channels)
print(img[0,0,:])

"""
plt.imshow(img)
plt.colorbar()
plt.show()
"""
float_img = img_as_float(img)
print(float_img[0,0,:])
ubyte_img = img_as_ubyte(float_img)
print(ubyte_img[0,0,:])