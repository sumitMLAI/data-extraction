from paddleocr import PaddleOCR
import cv2

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en') 

def image2text(image_path):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Perform OCR on the image
    result = ocr.ocr(image, cls=True)
    
    # Extract text
    text_list = []
    for line in result:
        for word in line:
            text_list.append(word[1][0])
    
    # Join the text into a single string
    invoice_data = " ".join(text_list)
    return invoice_data
# result=image2text(image_path='invoice.png')
# print(result)
