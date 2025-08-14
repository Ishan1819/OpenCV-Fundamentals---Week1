import cv2

image = cv2.imread("D:/img.jpg")

flipped_image = cv2.flip(image, 0)     # 0 is for vertical flipping and 1 is for mirror image

# Showing the original and flipped images
cv2.imshow("Original Image", image)
cv2.imshow("Flipped Image", flipped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()