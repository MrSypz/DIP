import cv2
import matplotlib.pyplot as plt
imgpath = "assets/2.7_cat_bw.png"
img = cv2.imread(imgpath)
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("image")
plt.subplot(1,2,2)
plt.hist(img.ravel(),256,[0,255])
plt.title("histogram")
plt.tight_layout()
plt.show()