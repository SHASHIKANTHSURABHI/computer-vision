import cv2
original_image = cv2.imread('original_image.jpg')
watermark_image = cv2.imread('watermark_image.png', cv2.IMREAD_UNCHANGED)
watermark_image_resized = cv2.resize(watermark_image, (original_image.shape[1], original_image.shape[0]))
alpha = 0.5
watermarked_image = cv2.addWeighted(original_image, 1 - alpha, watermark_image_resized, alpha, 0)
cv2.imwrite('watermarked_image.jpg', watermarked_image)
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
