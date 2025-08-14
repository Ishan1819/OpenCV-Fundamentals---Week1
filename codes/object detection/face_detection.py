import cv2
import os

# Haar cascade for face detection.load it from cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Path to input image
image_path = "D:/images.jpg"  

img = cv2.imread(image_path)

if img is None:
    print("Error: Could not read image. Check file path.")
    exit()
    
# preprocessing
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles across the faces. (0, 255, 0) for the color of border across the face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show count on image
cv2.putText(img, f"Faces detected: {len(faces)}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Saving the output image 
output_path = os.path.join(os.path.dirname(image_path), "face_output.jpg")
cv2.imwrite(output_path, img)

print(f"Output saved as {output_path}")

# Final image
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
