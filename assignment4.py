import cv2
gimg = cv2.imread('assets/2.1_cat.jpg',cv2.IMREAD_GRAYSCALE)
bwimg= cv2.threshold(gimg, 128,255,cv2.THRESH_BINARY)[1]
cv2.imshow("Black white image", bwimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('assets/2.7_cat_bw.png',bwimg)