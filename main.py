import os
from scripts.scraper import scrape_images
from scripts.generator import generate_synthetic_images
from scripts.augmentor import augment_images
from scripts.annotator import annotate_images
from scripts.exporter import export_dataset

def main():
    print("Welcome to the Computer Vision Dataset Builder CLI!")
    
    # Step 1: Image Scraping
    keyword = input("Enter keyword for scraping: ")
    num_images = int(input("How many images to scrape? "))
    scrape_images(keyword, num_images)

    # Step 2: Synthetic Image Generation
    generate_synthetic = input("Do you want to generate synthetic images? (yes/no): ").strip().lower()
    if generate_synthetic == 'yes':
        prompt = input("Enter prompt for synthetic image generation: ")
        image_count = int(input("How many synthetic images to generate? "))
        generate_synthetic_images(prompt, image_count)

    # Step 3: Image Augmentation
    augment_images()

    # Step 4: Auto Annotation
    annotate_choice = input("Do you want to annotate with YOLO or SAM? (yolo/sam): ").strip().lower()
    annotate_images(annotate_choice)

    # Step 5: Export Dataset
    export_format = input("Export format: yolo or coco? ").strip().lower()
    export_dataset(export_format)

if __name__ == "__main__":
    main()