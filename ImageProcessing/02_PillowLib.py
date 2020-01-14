# Excellent basic image manipulation for beginners
# pip install pillow
from PIL import Image
import numpy as np

img = Image.open("ImageProcessing/Images/asbbeaver.jpg")
print(type(img))  # type PIL image not numpy
print(img.format)
print("size:", img.size, " width:", img.width, " height:", img.height)
# img.show()

# convert to numpy array
np_img = np.asarray(img)
print("rows:", len(np_img), " columns:",len(np_img[0,:,0]))
print(type(np_img))
print("numpy image size:", np.size(np_img))

# resize to any size and crop "thumbnail" images only to smaller
small_img = img.resize((200, 100)) # no aspect ratio
small_img.save("ImageProcessing/Images/asbbeaver_a.jpg")

img.thumbnail((200,300)) # aspect repected so (200,117)
img.save("ImageProcessing/Images/asbbeaver_b.jpg")
print(img.size)

# image cropping
cropped_img = img.crop((0,0,100,100))
cropped_img.save("ImageProcessing/Images/asbbeaver_crop.jpg")

# image copy/paste
img_copy = img.copy()
img_copy.paste(cropped_img, (70, 10))
img_copy.save("ImageProcessing/Images/asbbeaver_copy_paste.jpg") 

# image rotation 
img_rot90 = img.rotate(90) # cropped while rotation
img_rot90.save("ImageProcessing/Images/asbbeaver_rot90.jpg")

img_rot45 = img.rotate(45, expand=True) # no cropping
img_rot45.save("ImageProcessing/Images/asbbeaver_rot45.jpg")

# image flipping
img_flipLR = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipLR.save("ImageProcessing/Images/asbbeaver_flipLR.jpg")

# gray scale conversion
img_gray = img.convert("L")
img_gray.save("ImageProcessing/Images/asbbeaver_gray.jpg")

# automating a task using glob "get file names"
# example 06_Varity

# save as PNG format
img.save("ImageProcessing/Images/asbbeaver_png.png","PNG")