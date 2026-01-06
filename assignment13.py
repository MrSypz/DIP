import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("assets/2.1_cat.jpg")
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("image")
color = ("b","g","r")
plt.subplot(1,2,2)
for channel,col in enumerate(color) :
    histr = cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.title("histogram")
plt.tight_layout()
plt.show()