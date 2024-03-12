from bin.storage import Storage
import unittest
import os

DOMAIN_URL = "test.com"
INDEX_PATH = "index.html"
TEST_INDEX_PATH = DOMAIN_URL + "/" + INDEX_PATH
CONTENT = "This is a test"


class TestStorage(unittest.TestCase):

    def test_save(self):
        storage = Storage(DOMAIN_URL)
        storage.save(INDEX_PATH, CONTENT)

        file_path = "{}{}".format(storage.BUILD_FOLDER, TEST_INDEX_PATH)
        file_created = os.path.exists(file_path)
        self.assertTrue(file_created)

    def test_read(self):
        storage = Storage(DOMAIN_URL)
        storage.save(INDEX_PATH, CONTENT)

        self.assertEqual(storage.read(INDEX_PATH), CONTENT)

    def test_create_folders(self):
        storage = Storage(DOMAIN_URL)
        storage.create_folders(TEST_INDEX_PATH)

        folder_path = "{}{}".format(storage.BUILD_FOLDER, DOMAIN_URL)
        folder_created = os.path.exists(folder_path)
        self.assertTrue(folder_created)

    def test_exist(self):
        storage = Storage(DOMAIN_URL)
        storage.save(INDEX_PATH, CONTENT)

        file_created = storage.exist(INDEX_PATH)
        self.assertTrue(file_created)


if __name__ == "__main__":
    unittest.main()
