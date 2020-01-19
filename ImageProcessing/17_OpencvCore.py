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
