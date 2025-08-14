import cv2

img = cv2.imread("D:/img.jpg")

# Coordinates of the face (x, y, width, height)
x, y, w, h = 200, 30, 150, 150  

face_region = img[y:y+h, x:x+w]

# Applying a blur to the face
face_blur = cv2.GaussianBlur(face_region, (99, 99), 30)

# Putting the blurred face back into the image
img[y:y+h, x:x+w] = face_blur

cv2.imshow("Blurred Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
