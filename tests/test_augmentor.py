import os
import cv2
import numpy as np
import pytest
from scripts.augmentor import augment_images

@pytest.fixture
def setup_images(tmp_path):
    raw_image_dir = tmp_path / "raw"
    augmented_image_dir = tmp_path / "augmented"
    os.makedirs(raw_image_dir)
    os.makedirs(augmented_image_dir)

    # Create a dummy image for testing
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite(str(raw_image_dir / "test_image.jpg"), image)

    return str(raw_image_dir), str(augmented_image_dir)

def test_augment_images(setup_images):
    raw_image_dir, augmented_image_dir = setup_images

    augment_images(raw_image_dir, augmented_image_dir)

    # Check if augmented images are saved
    augmented_images = os.listdir(augmented_image_dir)
    assert len(augmented_images) > 0

    # Check if the augmented images are valid images
    for img_file in augmented_images:
        img_path = os.path.join(augmented_image_dir, img_file)
        img = cv2.imread(img_path)
        assert img is not None
        assert img.shape == (100, 100, 3)  # Assuming augmentations do not change the image size

    # Additional checks can be added here for specific augmentations if needed