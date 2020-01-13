"""
# pip install opencv-python
# very advanced for basic image processing
# object recognition
"""
import cv2
from matplotlib import pyplot as plt

COLOR_IMG = cv2.imread("ImageProcessing/Images/flower1.jpg", 1) # optional color image 1
GRAY_IMG = cv2.imread("ImageProcessing/Images/flower1.jpg", 0)  # gray level image 0
print(type(GRAY_IMG))
"""
plt.imshow(COLOR_IMG)
plt.show()  # plotted colors are not correct, use cv2.imshow
"""
# plt didn't print colors correctly because cv2 colors are (BGR) not (RGB)
# so, plt.imshow(cv2.cvtColor(COLOR_IMG,cv2.COLOR_BGR2RGB))
# convert the BGR to RGB for plt to work
plt.imshow(cv2.cvtColor(COLOR_IMG, cv2.COLOR_BGR2RGB))
plt.show()

# or plot using cv2 commands
cv2.imshow("Color Image", COLOR_IMG)
cv2.imshow("Gray Image", GRAY_IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()
