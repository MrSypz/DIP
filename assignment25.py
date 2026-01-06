import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread("assets/3.1_cat.jpg",0)
img_float = img1.astype(np.float32)
img_min = np.min(img_float)
img_max = np.max(img_float)
minmax_img = 255 * (img_float - img_min) / (img_max - img_min)
minmax_img = minmax_img.astype(np.uint8)

plt.figure(num='Min Max', figsize=(8,4))
plt.subplot(1,2,1)
plt.title("Min Max Range")
plt.imshow(minmax_img, cmap='gray', vmin = 0, vmax=255)
plt.axis('off')
plt.subplot(1,2,2)
plt.hist(minmax_img.ravel(),bins = 256, range=(0,255))
plt.title("Histogram")
plt.xlabel("Bins")
plt.xlim([-10, 265])
plt.ylabel('Amounts of Pixels')
plt.tight_layout()
plt.show()