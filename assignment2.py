import cv2
img = cv2.imread('assets/2.1_cat.jpg',0)

print("Image Dimension  : ",img.shape)
print("Image Height     : ",img.shape[0])
print("Image Width      : ",img.shape[1])

cv2.imshow("Test Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('assets/2.4_cat_gray.jpg',img)

