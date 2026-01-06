from PIL import Image as img

import numpy as np

im = np.array(img.open('assets/2.3_eye.jpg'))
print(im.shape)
temp = im[25,55]
print(temp)
r,g,b = temp
print(r)
print(g)
print(b)