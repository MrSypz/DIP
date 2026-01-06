from PIL import Image 
from numpy import asarray

img = Image.open('assets/2.12_cat_g_trim.png')
img.show()
print("Image Size:",img.size)
print(asarray(img))