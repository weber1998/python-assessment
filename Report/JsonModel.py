class JsonModel:

    def __init__(self):
        self.data = []

    def set_data(self, data):
        self.data = data['presentation']

    def get_data(self):
        return self.data





