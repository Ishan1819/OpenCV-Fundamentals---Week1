import cv2
import matplotlib.pyplot as plt

# image in grayscale
img = cv2.imread("D:/img.jpg", cv2.IMREAD_GRAYSCALE)

# hisotgram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Displaying original image
cv2.imshow("Grayscale Image", img)

# Plot histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
