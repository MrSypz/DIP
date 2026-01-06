import cv2
gImg = cv2.imread('assets/3.1_cat.jpg',cv2.IMREAD_GRAYSCALE)
bwimg = cv2.threshold(gImg, 128, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('assets/3.2_cat_bw.png', bwimg)
bwimg_neg = 255 - bwimg
cv2.imshow("Input Image", bwimg)
cv2.imshow("Image Negative", bwimg_neg)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("assets/3.3_cat_bwimg_neg.png", bwimg_neg)