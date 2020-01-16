"""
testing various methods and utilities
"""
# testing glob
from glob import glob

PATH = "ImageProcessing/Images/*"
COUNT = len(glob(PATH))
for image_file in glob(PATH, recursive=True):
    print(image_file)

print("Number of files:", COUNT)

# testing plot
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(4, 4)

for i, ax in enumerate(axes.ravel()):
    im = ax.imshow(np.random.normal(size=100).reshape([10,10]))
    ax.set_title(i)

plt.tight_layout()
plt.show()