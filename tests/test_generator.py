import unittest
from scripts.generator import generate_images  # Assuming generate_images is the function to test

class TestImageGenerator(unittest.TestCase):

    def test_generate_images_valid_input(self):
        prompt = "A beautiful landscape"
        count = 5
        result = generate_images(prompt, count)
        self.assertEqual(len(result), count)
        # Add more assertions to check if the images are saved correctly

    def test_generate_images_zero_count(self):
        prompt = "A beautiful landscape"
        count = 0
        result = generate_images(prompt, count)
        self.assertEqual(len(result), 0)

    def test_generate_images_negative_count(self):
        prompt = "A beautiful landscape"
        count = -5
        with self.assertRaises(ValueError):
            generate_images(prompt, count)

    def test_generate_images_empty_prompt(self):
        prompt = ""
        count = 5
        with self.assertRaises(ValueError):
            generate_images(prompt, count)

if __name__ == '__main__':
    unittest.main()