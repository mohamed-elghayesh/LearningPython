# pip install matplotlib
# a powerful plotting tool that can read images
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread("ImageProcessing/Images/blur.jpg")
print(type(img))  # numpy ndarray
print("height:",img.shape[0]," width:", img.shape[1]," channels:", img.shape[2], img.shape)
plt.imshow(img)
plt.colorbar()
plt.show()