import cv2
import sys

images_paths = ["img_1.png", "img_2.png"]

images = []
for path in images_paths:
    img = cv2.imread(path)
    if img is None:
        print(f"Error reading image: {path}")
        sys.exit(1)
    images.append(img)

stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
(status, stitched) = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    print("Stitching successful!")
    output_path = "stitched_output.jpg"
    cv2.imwrite(output_path, stitched)
    print(f"Saved stitched image to: {output_path}")
else:
    print(f"Stitching failed with error code {status}")
