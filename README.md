# CV Dataset Builder CLI

## Overview
The CV Dataset Builder CLI is a Python-based command-line tool designed to facilitate the generation of large, high-quality computer vision datasets. This tool provides a modular pipeline that allows users to scrape images, generate synthetic images, augment datasets, auto-annotate images, and export datasets in various formats.

## Features
- **Image Scraping**: Download images from Google or Bing based on user-defined keywords.
- **Synthetic Image Generation**: Generate images using a locally hosted open-source diffusion model.
- **Image Augmentation**: Apply various augmentations to enhance the dataset quality.
- **Auto-Annotation**: Automatically annotate images using pre-trained models like YOLOv8 and SAM.
- **Export Options**: Export the final dataset in YOLO or COCO format with organized folder structures.

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd cv-dataset-builder-cli
pip install -r requirements.txt
```

## Usage
Run the CLI tool using the following command:

```bash
python main.py
```

Follow the prompts to:
1. Enter a keyword for scraping images.
2. Specify the number of images to scrape.
3. Choose whether to generate synthetic images.
4. Select the annotation method (YOLO or SAM).
5. Decide on the export format (YOLO or COCO).

## Folder Structure
The project is organized as follows:

```
cv-dataset-builder-cli
├── main.py                # Entry point for the CLI tool
├── requirements.txt       # List of dependencies
├── replit.nix            # Replit environment configuration
├── .replit                # Replit project settings
├── scripts                # Contains all modular scripts
│   ├── scraper.py         # Image scraping functionality
│   ├── generator.py       # Synthetic image generation
│   ├── augmentor.py       # Image augmentation
│   ├── annotator.py       # Image annotation
│   └── exporter.py        # Dataset export functionality
├── data                   # Directory for storing images
│   ├── raw                # Raw images from scraping
│   ├── generated          # Synthetic images
│   └── augmented          # Augmented images
├── tests                  # Unit tests for each module
│   ├── test_scraper.py    # Tests for scraper
│   ├── test_generator.py   # Tests for generator
│   ├── test_augmentor.py   # Tests for augmentor
│   ├── test_annotator.py   # Tests for annotator
│   └── test_exporter.py    # Tests for exporter
└── README.md              # Project documentation
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.