import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("assets/2.1_cat.jpg")
plt.imshow(img)
plt.show()
print(img.shape)
print(img[0,0])
rgb_img = np.flip(img,2)
print(rgb_img.shape)
print(rgb_img[0,0])
plt.imshow(rgb_img)
plt.show()

r_hist = cv2.calcHist([rgb_img],[0],None,[256],[0,256])
g_hist = cv2.calcHist([rgb_img],[1],None,[256],[0,256])
b_hist = cv2.calcHist([rgb_img],[2],None,[256],[0,256])
fig,axs = plt.subplots(1,3,figsize=(15,4),sharey=True)
axs[0].plot(r_hist,color="r")
axs[1].plot(g_hist,color="g")
axs[2].plot(b_hist,color="b")
plt.show()