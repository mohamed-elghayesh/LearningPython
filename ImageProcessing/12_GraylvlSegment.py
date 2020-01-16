# Gray level histogram segmentation, Threshold segmentation (global thresh, local thresh)
import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from scipy import ndimage

# plt read image to return numpy ndarray
img = plt.imread("ImageProcessing/Images/aeroplane.jpg")
plt.imshow(img)
plt.show()

gray_img = rgb2gray(img)
plt.title("Gray, (nrows, ncols): %s %s" %gray_img.shape)
plt.imshow(gray_img)
plt.show()

gray_r = gray_img.reshape(gray_img.shape[0]*gray_img.shape[1]) # flatting
print(gray_r.shape)

# use histogram to view positions of cuts fro local segmentation
plt.hist(gray_img.flat, bins=100) # 0:0.15, 0.15:0.25, 0.25:0.45,0.45:1
plt.show()

# global threshold segmentation using average pixel value
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 1
    else:
        gray_r[i] = 0

segmented_glob = gray_r.reshape(gray_img.shape[0],gray_img.shape[1])
plt.title("Segmented global, (nrows, ncols): %s %s" %segmented_glob.shape)
plt.imshow(segmented_glob, cmap="gray")
plt.show()

# local threshold segmentation using local averages found in histogram
gray_img = rgb2gray(img)
gray_c = gray_img.reshape(gray_img.shape[0]*gray_img.shape[1])
for i in range(gray_c.shape[0]):
    if gray_c[i] > 0.7:
        gray_c[i] = 2
    elif gray_c[i] > 0.3:
        gray_c[i] = 1
    else:
        gray_c[i] = 0

segmented_loc = gray_c.reshape(gray_img.shape[0],gray_img.shape[1])
plt.title("Segmented local, (nrows, ncols): %s %s" %segmented_loc.shape)
plt.imshow(segmented_loc, cmap="gray")
plt.show()
"""
plt.imshow(segmented_loc==2,cmap="gray")
plt.show()

plt.imshow(segmented_loc==1,cmap="gray")
plt.show()

plt.imshow(segmented_loc==0,cmap="gray")
plt.show() """

