import cv2
import numpy as np
input_image = cv2.imread('C:/Users/Shashikanth/OneDrive/Pictures/IMG_20220704_170818.png', cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(input_image, cv2.CV_64F, 1, 0, ksize=3) 
sobel_y = cv2.Sobel(input_image, cv2.CV_64F, 0, 1, ksize=3) 
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))
sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
cv2.imshow('Input Image', input_image)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
