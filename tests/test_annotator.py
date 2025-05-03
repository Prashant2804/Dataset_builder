import unittest
from scripts.annotator import Annotator

class TestAnnotator(unittest.TestCase):

    def setUp(self):
        self.annotator = Annotator()

    def test_yolo_annotation(self):
        # Assuming we have a test image and expected output
        test_image_path = 'data/raw/test_image.jpg'
        expected_output_path = 'annotations/test_image.json'
        
        # Run the annotation
        self.annotator.annotate_with_yolo(test_image_path)

        # Check if the output file exists
        self.assertTrue(os.path.exists(expected_output_path))

    def test_sam_annotation(self):
        # Assuming we have a test image and expected output
        test_image_path = 'data/raw/test_image.jpg'
        expected_output_path = 'annotations/test_image_segmentation.json'
        
        # Run the annotation
        self.annotator.annotate_with_sam(test_image_path)

        # Check if the output file exists
        self.assertTrue(os.path.exists(expected_output_path))

    def tearDown(self):
        # Clean up any created files after tests
        if os.path.exists('annotations/test_image.json'):
            os.remove('annotations/test_image.json')
        if os.path.exists('annotations/test_image_segmentation.json'):
            os.remove('annotations/test_image_segmentation.json')

if __name__ == '__main__':
    unittest.main()