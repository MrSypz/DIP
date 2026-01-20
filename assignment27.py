import cv2
import matplotlib.pyplot as plt

img = cv2.imread('assets/3.15_hist10x10.png', 0)
plt.figure(num='base', figsize=(8,4))
plt.hist(img.ravel(), 256, [0,255])
plt.title("Histogram")
plt.xlabel("Bins")
plt.xlim([-10, 265])
plt.ylabel('Amount of Pixels')
plt.tight_layout()
plt.show()
