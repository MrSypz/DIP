import cv2
img1 = cv2.imread('assets/3.1_cat.jpg')
img2 = cv2.imread('assets/3.20_reference_cat.png')
img = cv2.addWeighted(img1, 0.5, img2, 0.4,0)
cv2.imwrite('assets/3.21_addition_cat.png',img)
cv2.imshow('Addition Image', img)
cv2.waitKey(0)
cv2.destroyAllwindows()
