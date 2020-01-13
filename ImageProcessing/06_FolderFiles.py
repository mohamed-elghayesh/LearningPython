"""
testing various methods and utilities
"""

import glob

PATH = "ImageProcessing/Images/*"
COUNT = len(glob.glob(PATH))
for image_file in glob.glob(PATH, recursive=True):
    print(image_file)

print("Number of files:", COUNT)
