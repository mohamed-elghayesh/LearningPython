from scipy import misc
from scipy import ndimage
from matplotlib import pyplot as plt

img = misc.imread("ImageProcessing/Images/aeroplane.jpg")
print(type(img))
print(img.shape, img.dtype)

# scipy image rotation
rotated = ndimage.rotate(img,45,reshape=False)
plt.imshow(rotated)
plt.show()

# Scipy image filters : bluring
# gaussian is very powerful, edges are gone
# median preserves the edges
uniform_filter = ndimage.uniform_filter(img,size=9)
plt.imshow(uniform_filter)
plt.show()

gaussian_filter = ndimage.gaussian_filter(img,sigma=5)
plt.imshow(gaussian_filter)
plt.show()

median_filter = ndimage.median_filter(img,size=3)
plt.imshow(median_filter)
plt.show()

# Scipy image filters : edge detection
# sobel, finds horizontal (axis=0) and vertical lines (axis=1)
sobel_filter = ndimage.sobel(img, axis=1)
plt.imshow(sobel_filter)
plt.show()