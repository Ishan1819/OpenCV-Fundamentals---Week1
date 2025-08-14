import easyocr
import cv2

def extract_text_from_image(image_path):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'], gpu=False)

    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image at {image_path}")
        return

    # Perform OCR
    results = reader.readtext(img)

    # Printing extracted text
    print("\n[INFO] Extracted Text from Image:\n")
    for detection in results:
        text = detection[1]
        print(text)

if __name__ == "__main__":
    image_path = "Facts-about-cats.jpg"  
    extract_text_from_image(image_path)
