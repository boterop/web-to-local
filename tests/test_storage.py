import unittest
import os
from bin.storage import Storage

DOMAIN_URL = "test.com"
INDEX_PATH = "index.html"
TEST_INDEX_PATH = DOMAIN_URL + "/" + INDEX_PATH
CONTENT = "This is a test"


class TestStorage(unittest.TestCase):

    @staticmethod
    def clean():
        test_folder = Storage.BUILD_FOLDER + DOMAIN_URL
        Storage().remove(test_folder)

    def test_save(self):
        storage = Storage(DOMAIN_URL)
        storage.save(INDEX_PATH, CONTENT)
        file_path = "{}{}".format(storage.BUILD_FOLDER, TEST_INDEX_PATH)
        file_created = os.path.exists(file_path)

        self.assertTrue(file_created)
        self.clean()

    def test_read(self):
        storage = Storage(DOMAIN_URL)
        storage.save(INDEX_PATH, CONTENT)

        self.assertEqual(storage.read(INDEX_PATH), CONTENT)
        self.clean()

    def test_remove(self):
        storage = Storage(DOMAIN_URL)
        storage.save(INDEX_PATH, CONTENT)
        file_path = "{}{}".format(storage.BUILD_FOLDER, TEST_INDEX_PATH)
        self.assertTrue(os.path.exists(file_path))
        storage.remove(Storage.BUILD_FOLDER + DOMAIN_URL)
        self.assertFalse(os.path.exists(file_path))
        self.clean()

    def test_create_folders(self):
        storage = Storage(DOMAIN_URL)
        storage.create_folders(storage.BUILD_FOLDER + TEST_INDEX_PATH)

        folder_path = "{}{}".format(storage.BUILD_FOLDER, DOMAIN_URL)
        folder_created = os.path.exists(folder_path)

        self.assertTrue(folder_created)
        self.clean()

    def test_exist(self):
        storage = Storage(DOMAIN_URL)
        storage.save(INDEX_PATH, CONTENT)
        file_created = storage.exist(INDEX_PATH)

        self.assertTrue(file_created)
        self.clean()


if __name__ == "__main__":
    unittest.main()
