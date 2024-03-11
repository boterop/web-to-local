from bin.image_transform import ImageTransform
import unittest
import os

FILE_FOLDER = "tests/"
FILE_NAME = "image"
FILE_EXT = ".jpg"
FILE_PATH = FILE_FOLDER + FILE_NAME + FILE_EXT


class TestImageTransform(unittest.TestCase):

    def test_open(self):
        transform = ImageTransform(FILE_PATH)
        self.assertEqual(transform.image.filename, FILE_PATH)

    def test_resize(self):
        transform = ImageTransform(FILE_PATH)
        transform.resize(500, 500)
        
        self.assertNotEqual(transform.image.size, transform.new_image.size)
        self.assertEqual((500, 500), transform.new_image.size)

    def test_save(self):
        transform = ImageTransform(FILE_PATH)
        transform.resize(500, 500)
        test_image_path = FILE_FOLDER + FILE_NAME + "_test" + FILE_EXT
        transform.save(test_image_path)

        self.assertTrue(os.path.exists(test_image_path))
        self.assertTrue(os.path.isfile(test_image_path))

    def test_round(self):
        transform = ImageTransform(FILE_PATH)
        transform.resize(500, 500)
        img1 = transform.new_image
        transform.round()
        img2 = transform.new_image
        
        self.assertNotEqual(img1, img2)


if __name__ == "__main__":
    unittest.main()
