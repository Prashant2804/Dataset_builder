import os
import json
import shutil

def export_dataset(export_format, dataset_path, output_path):
    if export_format == 'yolo':
        export_yolo(dataset_path, output_path)
    elif export_format == 'coco':
        export_coco(dataset_path, output_path)
    else:
        raise ValueError("Unsupported export format. Choose 'yolo' or 'coco'.")

def export_yolo(dataset_path, output_path):
    os.makedirs(os.path.join(output_path, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_path, 'labels'), exist_ok=True)

    # Copy images and labels to the respective folders
    for label_file in os.listdir(os.path.join(dataset_path, 'labels')):
        shutil.copy(os.path.join(dataset_path, 'labels', label_file), os.path.join(output_path, 'labels', label_file))
    
    for image_file in os.listdir(os.path.join(dataset_path, 'images')):
        shutil.copy(os.path.join(dataset_path, 'images', image_file), os.path.join(output_path, 'images', image_file))

def export_coco(dataset_path, output_path):
    coco_format = {
        "images": [],
        "annotations": [],
        "categories": []
    }

    # Populate the COCO format structure
    # This is a placeholder for actual implementation
    # You would need to read images and annotations and fill the coco_format dictionary

    with open(os.path.join(output_path, 'annotations.json'), 'w') as json_file:
        json.dump(coco_format, json_file)

def main():
    # Example usage
    export_format = input("Export format (yolo/coco): ")
    dataset_path = input("Enter the path to the dataset: ")
    output_path = input("Enter the output path: ")
    
    export_dataset(export_format, dataset_path, output_path)

if __name__ == "__main__":
    main()