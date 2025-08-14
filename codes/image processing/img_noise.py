import cv2
import numpy as np

# Read the image
img = cv2.imread("D:/img.jpg")

# 1. Blurring (Gaussian Blur)
blurred = cv2.GaussianBlur(img, (15, 15), 0)  # (kernel size, sigmaX)

# 2. Sharpening
# Create a sharpening kernel
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, sharpen_kernel)

# Show results
cv2.imshow("Original", img)
cv2.imshow("Blurred", blurred)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
