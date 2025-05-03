import os
import cv2
import glob
import albumentations as A

def augment_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define augmentation pipeline
    augmentation_pipeline = A.Compose([
        A.RandomRotate90(),
        A.HorizontalFlip(),
        A.VerticalFlip(),
        A.RandomBrightnessContrast(),
        A.Blur(blur_limit=3),
        A.MultiplicativeNoise(),
        A.Crop(x_min=0, y_min=0, x_max=256, y_max=256),  # Adjust crop size as needed
        A.Mosaic(),
    ])

    # Process each image in the input folder
    for image_path in glob.glob(os.path.join(input_folder, '*')):
        image = cv2.imread(image_path)
        if image is not None:
            augmented = augmentation_pipeline(image=image)
            augmented_image = augmented['image']
            output_path = os.path.join(output_folder, os.path.basename(image_path))
            cv2.imwrite(output_path, augmented_image)

def augment_raw_images():
    raw_data_folder = 'data/raw/'
    augmented_data_folder = 'data/augmented/raw/'
    for keyword in os.listdir(raw_data_folder):
        augment_images(os.path.join(raw_data_folder, keyword), os.path.join(augmented_data_folder, keyword))

def augment_generated_images():
    generated_data_folder = 'data/generated/'
    augmented_data_folder = 'data/augmented/generated/'
    for prompt in os.listdir(generated_data_folder):
        augment_images(os.path.join(generated_data_folder, prompt), os.path.join(augmented_data_folder, prompt))

if __name__ == "__main__":
    augment_raw_images()
    augment_generated_images()