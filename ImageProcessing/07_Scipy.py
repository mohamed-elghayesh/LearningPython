from scipy import misc

img = misc.imread("ImageProcessing/Images/flower1.jpg")
print(type(img))
print(img.shape, img.dtype)
