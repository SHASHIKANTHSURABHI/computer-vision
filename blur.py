import cv2
image=cv2.imread("C:/Users/Shashikanth/OneDrive/Pictures/IMG_20220704_170818.png")
cv2.imshow('original',image)
cv2.waitKey(0)
blur=cv2.GaussianBlur(image,(9,9),cv2.BORDER_DEFAULT)
cv2.imshow("blur image",blur)
cv2.waitKey(0)
