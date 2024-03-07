import cv2
image=cv2.imread("C:/Users/Shashikanth/OneDrive/Pictures/IMG_20220704_170818.png")
cv2.imshow('original',image)
resized=cv2.resize(image,(300,300),interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized to small",resized)
cv2.waitKey(0)
resized=cv2.resize(image,(1000,1000),interpolation=cv2.INTER_AREA)
cv2.imshow("resized to big",resized)
cv2.waitKey(0)
