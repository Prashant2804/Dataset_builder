import os
import cv2
import numpy as np
from ultralytics import YOLO

class Annotator:
    def __init__(self, model_path='yolov8.pt'):
        self.model = YOLO(model_path)

    def annotate_images(self, image_folder, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for image_name in os.listdir(image_folder):
            image_path = os.path.join(image_folder, image_name)
            if image_path.endswith(('.png', '.jpg', '.jpeg')):
                self.annotate_image(image_path, output_folder)

    def annotate_image(self, image_path, output_folder):
        image = cv2.imread(image_path)
        results = self.model(image)

        # Draw bounding boxes on the image
        for result in results:
            boxes = result.boxes.xyxy.numpy()  # Get bounding box coordinates
            for box in boxes:
                x1, y1, x2, y2 = map(int, box[:4])
                cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

        output_path = os.path.join(output_folder, os.path.basename(image_path))
        cv2.imwrite(output_path, image)

    def save_annotations(self, results, output_folder):
        # Implement saving annotations in a standard format
        pass

if __name__ == "__main__":
    annotator = Annotator()
    annotator.annotate_images('data/raw/', 'annotations/')  # Example usage