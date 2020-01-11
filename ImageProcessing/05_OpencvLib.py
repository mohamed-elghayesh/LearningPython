# pip install opencv-python
# very advanced for basic image processing
# object recognition
import cv2
from matplotlib import pyplot as plt

# img = cv2.imread("ImageProcessing/Images/asbbeaver.jpg")
img = cv2.imread("ImageProcessing/Images/blur.jpg")  # gray level image
print(type(img))
"""
plt.imshow(img)
plt.show()  # plotted colors are not correct, use cv2.imshow
"""
cv2.imshow("Test Image",img)
cv2.waitKey(0)