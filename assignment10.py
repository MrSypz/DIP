from PIL import Image
import numpy as np
img = np.array(Image.open('assets/2.1_cat.jpg'))
print(img.shape)
im_trim = img[460:470, 200:215]
print(im_trim.shape)
Image.fromarray(im_trim).save('assets/2.16_cat_trim.png')
img = Image.open("assets/2.16_cat_trim.png")
img.show()