import os

class Utils:
    def __init__(self):
        pass

    def createDirectory(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)

    def listDir(self, dir):
        return os.listdir(dir)
    
    def loadFile(self, file_name_path):
        with open(file_name_path, "r") as f:
            return f.read()