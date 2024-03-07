#dilating image
import cv2
image=cv2.imread("C:/Users/Shashikanth/OneDrive/Pictures/IMG_20220704_170818.png")
cv2.imshow('original',image)
dilated=cv2.dilate(image,(100,100),iterations=1)
cv2.imshow("dialated",dilated)
cv2.waitKey(0)
