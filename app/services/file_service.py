import json


class FileService:

    @staticmethod
    def read_json(path):

        with open(path, "r") as file:
            return json.load(file)

    @staticmethod
    def write_json(path, data):

        with open(path, "w") as file:
            json.dump(data, file, indent=4)
