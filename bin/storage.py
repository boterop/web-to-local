import os
import shutil


class Storage:
    BUILD_FOLDER = "build/"

    def __init__(self, path: str):
        build_path = self.BUILD_FOLDER + path + "/"
        self.path = build_path
        
        if os.path.exists(build_path):
            shutil.rmtree(build_path)

        folder_path = ""
        for folder in build_path.split("/"):
            folder_path += folder + "/"
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

    def save(self, fileName: str, content: str):
        file = open(self.path + fileName, "a")
        try:
            file.write(content)
        finally:
            file.close()
