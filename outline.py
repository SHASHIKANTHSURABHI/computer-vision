import cv2
image=cv2.imread("C:/Users/Shashikanth/OneDrive/Pictures/IMG_20220704_170818.png")
canny=cv2.Canny(image,125,125)
cv2.imshow("canny edges",canny)
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
cv2.waitKey(0)
