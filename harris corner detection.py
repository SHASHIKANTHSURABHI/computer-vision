import cv2
import numpy as np
image = cv2.imread('C:/Users/Shashikanth/OneDrive/Pictures/IMG_20220704_170818.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image_float32 = np.float32(gray_image)
harris_corners = cv2.cornerHarris(gray_image_float32, 2, 3, 0.04)
harris_corners_norm = cv2.normalize(harris_corners, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
threshold = 0.01 * harris_corners_norm.max()
corner_image = np.zeros_like(image)
corner_image[harris_corners_norm > threshold] = [0, 0, 255]  
cv2.imshow('Original Image', image)
cv2.imshow('Harris Corner Detection', corner_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
