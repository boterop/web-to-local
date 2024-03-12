import os
import shutil


class Storage:
    BUILD_FOLDER = "build/"

    def __init__(self, path: str):
        build_path = self.BUILD_FOLDER + path + "/"
        self.path = build_path
        self.create_folders(build_path)

    def save(self, file_path: str, content: str):
        path = self.path + file_path
        folder = "/".join(path.split("/")[0:-1])
        self.create_folders(folder)
        file = open(path, "a")
        try:
            file.write(content)
        finally:
            file.close()

    def read(self, file_path: str):
        path = self.path + file_path
        file = open(path, "r")

        content = ""
        try:
            content = file.read()
        finally:
            file.close()

        return content

    def create_folders(self, path: str):
        if os.path.exists(path):
            shutil.rmtree(path)

        folder_path = ""
        for folder in path.split("/"):
            folder_path += folder + "/"
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

    def exist(self, file_path: str):
        return os.path.exists(self.path + file_path)
