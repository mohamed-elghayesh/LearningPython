# This is a basic segmentation example that calculates
# the percent of wound healing / scratch assay

import matplotlib.pyplot as plt
import numpy as np
from skimage import io, restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import try_all_threshold, gaussian, threshold_otsu

# entropy is the amount
img = io.imread("ImageProcessing/Images/wound1.jpg",as_gray=True)
gauss_img = gaussian(img,1)
entropy_img = entropy(gauss_img, disk(40))  # vary disk size for cleaner results

fig, ax = try_all_threshold(entropy_img, figsize=(10,8), verbose=False)
plt.show()

thresh = threshold_otsu(entropy_img) # returns the best threshold value
binary_img = entropy_img <= thresh # if entropy_img is LE thresh return True else False
plt.imshow(binary_img,cmap="gray")
plt.show()

pixels_sum = binary_img.shape[0] * binary_img.shape[1]
print("The percent of bright pixels is:", np.sum(binary_img==1)/pixels_sum)
