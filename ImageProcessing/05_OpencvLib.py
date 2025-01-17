"""
# pip install opencv-python
# pip install -U --target="C:\python_path\Lib" opencv-python
# 
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

# reading and showing a captured video
cap = cv2.VideoCapture(0)

# cap.get(i=0-18), width i=3, height i=4, fps i=5
print(cap.get(3),cap.get(4), cap.get(5))

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret, frame = cap.read()
    
    # convert to gray frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #out.write(frame)
    cv2.imshow("Video Test", gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

# when every thing closes release the capture
cap.release()
cv2.destroyAllWindows()
