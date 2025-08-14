import cv2
import numpy as np

# Creating two simple black images
img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

# white rectangle on img1
cv2.rectangle(img1, (50, 50), (250, 250), 255, -1)

#white circle on img2
cv2.circle(img2, (150, 150), 100, 255, -1)

# bitwise operations
bitwise_and = cv2.bitwise_and(img1, img2)  # AND
bitwise_or = cv2.bitwise_or(img1, img2)    # OR
bitwise_xor = cv2.bitwise_xor(img1, img2)  # XOR
bitwise_not_img1 = cv2.bitwise_not(img1)   # NOT on img1

# Display results
cv2.imshow("Image 1 (Rectangle)", img1)
cv2.imshow("Image 2 (Circle)", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("XOR", bitwise_xor)
cv2.imshow("NOT (Image 1)", bitwise_not_img1)

cv2.waitKey(0)
cv2.destroyAllWindows()






