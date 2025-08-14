import cv2
import numpy as np

img = np.zeros((300, 300, 3), dtype=np.uint8)
img[:] = (210, 120, 100)  # background

# circle in between
cv2.circle(img, (150, 150), 80, (100, 120, 210), -1)


# Displaying the image
cv2.imshow("Intro Test Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
