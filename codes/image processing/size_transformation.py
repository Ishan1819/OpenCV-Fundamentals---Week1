import cv2

# Read image
img = cv2.imread("D:/img.jpg")

# Resize smaller (50% of original size)
small = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Resize bigger (150% of original size)
big = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Original", img)
cv2.imshow("Smaller", small)
cv2.imshow("Bigger", big)

cv2.waitKey(0)
cv2.destroyAllWindows()
