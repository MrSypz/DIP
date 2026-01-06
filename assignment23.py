import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("assets/3.1_cat.jpg",0)
high_con = img.copy()

for y in range(img.shape[0]) :
    for x in range(img.shape[1]) :
        a = 1.1
        b = 0
        high_con[y,x] = np.clip(a * img[y,x] + b, 0 , 255)

plt.figure(num='My_Cat', figsize=(8,4))
plt.subplot(1,2,1)
plt.title("High Contrast")
plt.imshow(high_con, cmap='gray', vmin = 0, vmax=255)
plt.axis('off')
plt.subplot(1,2,2)
plt.hist(high_con.ravel(),256,[0,255])
plt.title("High Contrast Histogram")
plt.xlabel("Bins")
plt.xlim([-10, 265])
plt.ylabel('Amounts of Pixels')
plt.tight_layout()
plt.show()