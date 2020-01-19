# core operations: ROI region of interest
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import animation as anim

img = cv2.imread("ImageProcessing/Images/messi.jpg")
print(img.shape)
cv2.imshow("Messi", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# copy the ball to other location
ball = img[287:337, 337:388]
img[280:330, 137:188] = ball
#cv2.imwrite("ImageProcessing/Images/messi_2balls.jpg",img)

# TODO: try to detect the fake ball in the messi_2balls.jpg image
# convert to gray, maybe bool, check for artifacts

# splitting an image into B,G,R channels then Merging them again
# img[:,:,0] -> B, img[:,:,1] -> G, img[:,:,2] -> R, much more efficient than cv2.split()
b,g,r = cv2.split(img)
img = cv2.merge((g,g,b))
cv2.imshow("Messi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Arithmetic operations: Image addition
# cv2 addition (all above 255 = 255) saturated -> cv2.add(x,y)
# numpy addition (result % 256) modulo -> x + y
# blending is also addition (1 - a)x + ay .. a varies 0-1 
img1 = cv2.imread("ImageProcessing/Images/hurrah1.jpg")
img2 = cv2.imread("ImageProcessing/Images/hurrah2.jpg")
imgs = []
fig = plt.figure()

for i in range(101):
    dst = cv2.addWeighted(img1,i/100,img2,1-i/100,0)
    im = plt.imshow(dst, animated=True)
    imgs.append([im]) # im must be read as list to be animated

ani = anim.ArtistAnimation(fig, imgs, 100)
plt.show()

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

# Bitwise operations
# Load two images
img1 = cv2.imread('ImageProcessing/Images/messi.jpg')
img2 = cv2.imread('ImageProcessing/Images/opencv.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 20, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# performance measurement using opencv
# cv2.useOptimized() to check cv2 runs optimized code
"""
e1 = cv2.getTickCount()
# code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
# also using time module
t1 = time.time()
# code 
t2 = time.time()
span = t2 - t1
"""
