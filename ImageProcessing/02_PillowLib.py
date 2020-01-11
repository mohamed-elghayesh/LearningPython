# Excellent basic image manipulation for beginners
# pip install pillow
from PIL import Image
import numpy as np

img = Image.open("ImageProcessing/Images/asbbeaver.jpg")
print(type(img))  # type PIL image not numpy
print(img.format)
print("size:",img.size," width:",img.width," height:",img.height)
# img.show()

# convert to numpy array
np_img = np.asarray(img)
print("rows:",len(np_img)," columns:",len(np_img[0,:,0]))
print(type(np_img))
print("np.size:",np.size(np_img))