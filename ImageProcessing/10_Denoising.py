# beside cleaning, removing high signal noise, is a prequisite for segmentation
# filters: median, non local means, gaussian 
import numpy as np
from skimage import io, img_as_float
from scipy import ndimage as nd
from matplotlib import pyplot as plt 
from skimage.restoration import denoise_nl_means, estimate_sigma

img = io.imread("ImageProcessing/Images/cell1.jpg")

# with gaussian we lose information and bluring occures
gaussian_img = nd.gaussian_filter(img, sigma=3)
plt.imsave("ImageProcessing/Images/cell1_gaussian.jpg",gaussian_img)

# excellent for denoising while preserving edges no bluring
median_img = nd.median_filter(img, size=3)
plt.imsave("ImageProcessing/Images/cell1_median.jpg",median_img)

# non local means filter: perfect for nosie reduction preserving edges
sigma_est = np.mean(estimate_sigma(img, multichannel=True))
flt_img = img_as_float(img)
nlmeans_img = denoise_nl_means(flt_img, h=1.15*sigma_est, fast_mode=True, patch_size=5, patch_distance=3, multichannel=True)
plt.imsave("ImageProcessing/Images/cell1_nlmeans.jpg",nlmeans_img)
