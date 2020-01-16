# Random walker segmantation technique
from skimage import io, img_as_float
from skimage.exposure import rescale_intensity, equalize_adapthist
from skimage.data import binary_blobs
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage.segmentation import random_walker
from matplotlib import pyplot as plt 
import numpy as np 

# Generate noisy synthetic data
data = img_as_float(binary_blobs(length=128, seed=1))
sigma = 0.25
data += np.random.normal(loc=0, scale=sigma, size=data.shape)
data = rescale_intensity(data, in_range=(-sigma, 1 + sigma), out_range=(-1, 1))
plt.imshow(data, cmap="gray")
plt.show()

#img = img_as_float(io.imread("ImageProcessing/Images/walker.png"))
plt.hist(data.flat, bins=100, range=(0,1))
plt.show()

# equalizing data histogram
eq_data = equalize_adapthist(data)
plt.hist(eq_data.flat, bins=100, range=(0,1))
plt.show()

plt.imshow(eq_data, cmap="gray")
plt.show()

# denoising before segmentation
sigma_est = np.mean(estimate_sigma(data, multichannel=True))
patch_kw = dict(patch_size=5, patch_distance=6, multichannel=True)
denoised_img = denoise_nl_means(eq_data,h=1.15 * sigma_est,fast_mode=True,**patch_kw)

eq_img = equalize_adapthist(denoised_img)
plt.hist(eq_img.flat, bins=100, range=(0,1))
plt.show()

plt.imshow(eq_img, cmap="gray")
plt.show()

# define some markers for kick starting random walker segmentation
markers = np.zeros(data.shape, dtype=np.uint)
markers[(eq_img > 0.1) & (eq_img < 0.4)] = 1
markers[(eq_img > 0.5) & (eq_img < 0.99)] = 2

plt.imshow(markers)
plt.show()

# random walker segmentation
labels = random_walker(eq_img, markers, beta=10, mode="bf")
plt.imshow(labels)
plt.show()

# trying to make segments
segm1 = (labels == 1)
segm2 = (labels == 2)
all_segms = np.zeros((eq_img.shape[0],eq_img.shape[0],3))
all_segms[segm1] = (1,0,0)
all_segms[segm2] = (0,1,0)
plt.imshow(all_segms)
plt.show()