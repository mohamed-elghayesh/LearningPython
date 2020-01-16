# reading multiple images for the same wound at different times
# calculating the healing rate and other stats
from skimage import io
from matplotlib import pyplot as plt
import numpy as np 
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import threshold_otsu
import glob
from scipy.stats import linregress

time = 0
time_list = []
area_list = []
path = "ImageProcessing/Images/Wounds/*"

for img_file in glob.glob(path):
    img = io.imread(img_file,as_gray=True)
    entropy_img = entropy(img,disk(40))
    thresh = threshold_otsu(entropy_img) # auto thresholding method
    binary = entropy_img <= thresh
    scratch_area = np.sum(binary == True)
    print(time, scratch_area)
    time_list.append(time)
    area_list.append(scratch_area)
    time += 1
print(time_list, area_list)
plt.plot(time_list, area_list, 'ro')
print(linregress(time_list, area_list))
plt.show()





