import cv2
img = cv2.imread("assets/2.1_cat.jpg")
print("Original Dimentioms :",img.shape)
width = 150
height = 200
dim = (width,height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
print("Resized Dimentios :",resized.shape)
print("Image Height :",resized.shape[0])
print("Image Width :",resized.shape[1])
print("Number of Channals :",resized.shape[2])
cv2.imshow("Resized image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("assets/2.32_cat_150x200.jpg",resized)