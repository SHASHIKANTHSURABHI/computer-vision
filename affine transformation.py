import cv2
import numpy as np
image = cv2.imread('C:/Users/Shashikanth/OneDrive/Pictures/IMG_20220704_170818.png')
angle = 45  
scale = 1.5  
tx = 50     
ty = 30     
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, scale)
transformation_matrix = np.dot(rotation_matrix, np.vstack((translation_matrix, [0, 0, 1])))
output_image = cv2.warpAffine(image, transformation_matrix, (image.shape[1], image.shape[0]))
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
