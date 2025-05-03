import unittest
from scripts.scraper import scrape_images  # Adjust the import based on your actual function name

class TestImageScraper(unittest.TestCase):

    def test_scrape_images_valid_keyword(self):
        keyword = "cats"
        num_images = 5
        result = scrape_images(keyword, num_images)
        self.assertTrue(len(result) <= num_images)
        self.assertTrue(all(isinstance(img, str) for img in result))  # Assuming the function returns a list of image paths

    def test_scrape_images_invalid_keyword(self):
        keyword = ""
        num_images = 5
        with self.assertRaises(ValueError):  # Adjust based on your error handling
            scrape_images(keyword, num_images)

    def test_scrape_images_zero_count(self):
        keyword = "dogs"
        num_images = 0
        result = scrape_images(keyword, num_images)
        self.assertEqual(result, [])  # Assuming it returns an empty list for zero images

if __name__ == '__main__':
    unittest.main()