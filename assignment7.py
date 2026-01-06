import cv2
gimg = cv2.imread("assets/2.1_cat.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Gray image", gimg)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('assets/2.6_cat_g.png',gimg)