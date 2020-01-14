# pip install scikit-image
from skimage import io, img_as_float, img_as_ubyte
from matplotlib import pyplot as plt
from scipy import ndimage
import numpy as np

img = io.imread("ImageProcessing/Images/flower1.jpg")
print("type read image:", type(img)) # numpy ndarray
print("(width, height, channels):", img.shape) # tuple of (width,height,channels)

"""
plt.imshow(img)
plt.colorbar()
plt.show()
"""
float_img = img_as_float(img)
print("float_img first pixel:", float_img[0,0,:])
ubyte_img = img_as_ubyte(float_img)
print("utype_img first pixel:", ubyte_img[0,0,:])

print("float_img datatype:", float_img.dtype)
print("utype_img datatype:", ubyte_img.dtype)

# gray image
gray_img = io.imread("ImageProcessing/Images/flower1.jpg", as_gray=True)
print("gray_img[0,0] = ", gray_img[0,0])

mean_gray = gray_img.mean()
max_value = gray_img.max()
min_value = gray_img.min()

print("Min, Max, and Mean:", min_value, max_value, mean_gray)

# flip LR ,need numpy
flipped_LR = np.fliplr(gray_img)
flipped_UD = np.flipud(gray_img)

# plotting sub-plots 
"""
fig, ax = plt.subplots()
ax.imshow(gray_img)
plt.show()
"""
fig, ax = plt.subplots(2,2)
ax[0,0].imshow(img)
ax[0,0].set_title('RGB')
ax[0,1].imshow(gray_img, cmap="Greys") # change color map
ax[0,1].set_title('Gray')
ax[1,0].imshow(flipped_LR)
ax[1,0].set_title('Flip LR')
ax[1,1].imshow(flipped_UD)
ax[1,1].set_title('Flip UD')

plt.tight_layout()  # plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()
