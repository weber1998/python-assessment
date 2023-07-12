import json

class JsonModel:

    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def save_model(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(self.data))
    def get_data(self):
        return self.data





