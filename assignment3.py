from PIL import Image

from numpy import asarray

img = Image.open("assets/2.4_cat_gray.jpg")
img.show()
print("Image Size:", img.size)
data=asarray(img)
print("Image Data as 0,1    :\n",data[0,1])
print("Image Data as 0      :\n",data[0])
print("Image Pure Data      :\n",data)