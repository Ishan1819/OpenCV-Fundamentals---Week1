import cv2

# Path to input image
input_image_path = "images.jpg"  

# Load the image
image = cv2.imread(input_image_path)
if image is None:
    raise FileNotFoundError(f"Image '{input_image_path}' not found.")

# download cars.xml from here and put it below https://github.com/andrewssobral/vehicle_detection_haarcascades
cascade_path = "cars.xml"  
car_cascade = cv2.CascadeClassifier(cascade_path)

if car_cascade.empty():
    raise FileNotFoundError(f"Cascade file '{cascade_path}' not found.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, 1.1, 2)

# Draw rectangles around detected cars
for (x, y, w, h) in cars:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(f"Detected {len(cars)} vehicles.")

# save the output image in the same directory
output_image_path = "road_with_vehicles.jpg"
cv2.imwrite(output_image_path, image)

print(f"Output saved as '{output_image_path}'")
