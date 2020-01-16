# pip install scikit-image
from skimage import io, img_as_float, img_as_ubyte
from skimage.transform import rescale,resize,downscale_local_mean
from skimage.filters import roberts, sobel, scharr, prewitt
from matplotlib import pyplot as plt
import numpy as np

# read image using scikit
img = io.imread("ImageProcessing/Images/aeroplane.jpg")
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

# scikit gray image
gray_img = io.imread("ImageProcessing/Images/aeroplane.jpg", as_gray=True)
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
ax[1,0].imshow(flipped_LR, cmap="Reds")
ax[1,0].set_title('Flip LR')
ax[1,1].imshow(flipped_UD, cmap= "hsv")
ax[1,1].set_title('Flip UD')

plt.tight_layout()  # plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()

# rescaling an image
rescaled_img = rescale(gray_img,1.0/4.0,anti_aliasing=True)
resized_img = resize(gray_img,(200,200))
downscaled_img = downscale_local_mean(gray_img,(4,3))

plt.imshow(downscaled_img)
plt.show()

# skimage.filters : Edge detection
# roberts, sobel, scharr, prewitt
edge_roberts = roberts(gray_img)
edge_sobel = sobel(gray_img)
edge_scharr = scharr(gray_img)
edge_prewitt = prewitt(gray_img)

# noise reduction, gradient calculation, edge detection and tracking
from skimage.feature import canny
edge_canny = canny(gray_img, 1.5) # bigger sigma fewer edges

fig, ax = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True,figsize=(8,8))
axe = ax.ravel()
axe[0].imshow(gray_img)
axe[0].set_title("Original Image")
axe[1].imshow(edge_roberts)
axe[1].set_title("Robert Edge Detection")
axe[2].imshow(edge_sobel)
axe[2].set_title("Sobel Edge Detection")
axe[3].imshow(edge_scharr)
axe[3].set_title("Scharr Edge Detection")
axe[4].imshow(edge_prewitt)
axe[4].set_title("Prewitt Edge Detection")
axe[5].imshow(edge_canny)
axe[5].set_title("Canny Edge Detection")
plt.show()

# deconvolution overcomes light spread using point spread function psf
from skimage import restoration

psf = np.ones((3,3))/9
deconvolved, _ = restoration.unsupervised_wiener(gray_img,psf)
plt.imsave("ImageProcessing/Images/aeroplane_deconvolved.jpg",deconvolved,cmap="gray")
