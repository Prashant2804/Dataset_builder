import os
import unittest
from scripts.exporter import Exporter

class TestExporter(unittest.TestCase):

    def setUp(self):
        self.exporter = Exporter()
        self.test_data_path = 'data/test/'
        os.makedirs(self.test_data_path, exist_ok=True)

    def tearDown(self):
        for filename in os.listdir(self.test_data_path):
            file_path = os.path.join(self.test_data_path, filename)
            os.remove(file_path)
        os.rmdir(self.test_data_path)

    def test_export_yolo_format(self):
        # Assuming the exporter has a method to export in YOLO format
        self.exporter.export(self.test_data_path, format='yolo')
        # Check if the expected files are created
        self.assertTrue(os.path.exists(os.path.join(self.test_data_path, 'images')))
        self.assertTrue(os.path.exists(os.path.join(self.test_data_path, 'labels')))

    def test_export_coco_format(self):
        # Assuming the exporter has a method to export in COCO format
        self.exporter.export(self.test_data_path, format='coco')
        # Check if the expected COCO file is created
        self.assertTrue(os.path.exists(os.path.join(self.test_data_path, 'annotations.json')))

    def test_export_invalid_format(self):
        with self.assertRaises(ValueError):
            self.exporter.export(self.test_data_path, format='invalid_format')

if __name__ == '__main__':
    unittest.main()