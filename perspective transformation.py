import cv2
import numpy as np
image = cv2.imread('C:/Users/Shashikanth/OneDrive/Pictures/IMG_20220704_170818.png')
original_points = np.float32([[0, 0], [image.shape[1], 0], [0, image.shape[0]], [image.shape[1], image.shape[0]]])
desired_points = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
perspective_matrix = cv2.getPerspectiveTransform(original_points, desired_points)
output_image = cv2.warpPerspective(image, perspective_matrix, (300, 300))  # Size of the output image
cv2.imshow('Original Image', image)
cv2.imshow('Perspective Transformed Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
