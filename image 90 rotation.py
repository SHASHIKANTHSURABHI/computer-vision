import cv2
image=cv2.imread("C:/Users/Shashikanth/OneDrive/Pictures/IMG_20220704_170818.png")
cv2.imshow('original',image)
def rotate(image,angle,rotpoint=None):
    (height,width)=image.shape[:2]
    if(rotpoint is None):
        rotpoint=(width//2,height//2)
    rotmat=cv2.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=[width,height]
    return cv2.warpAffine(image,rotmat,dimensions)
rotated=rotate(image,-270)
cv2.imshow("rotated",rotated)
cv2.waitKey(0)
