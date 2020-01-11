# pip install opencv-python
# very advanced for basic image processing
# object recognition
import cv2
from matplotlib import pyplot as plt

color_img = cv2.imread("ImageProcessing/Images/blur.jpg",1) # optional color image 1
gray_img = cv2.imread("ImageProcessing/Images/blur.jpg",0)  # gray level image 0
print(type(gray_img))
plt.imshow(color_img)
plt.show()  # plotted colors are not correct, use cv2.imshow
"""
# plt didn't print colors correctly because cv2 colors are (BGR) not (RGB)
# so, plt.imshow(cv2.cvtColor(color_img,cv2.COLOR_BGR2RGB))
# convert the BGR to RGB for plt to work
plt.imshow(cv2.cvtColor(color_img,cv2.COLOR_BGR2RGB))
plt.show()

# or plot using cv2 commands
cv2.imshow("Color Image",color_img)
cv2.imshow("Gray Image",gray_img)
cv2.waitKey(0)
"""