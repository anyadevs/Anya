class BaseModel:
    def __init__(self):
        self.trained = False

    def train(self, data):
        raise NotImplementedError("Train method must be implemented by subclasses.")

    def predict(self, input_data):
        raise NotImplementedError("Predict method must be implemented by subclasses.")

    def save(self, file_path):
        raise NotImplementedError("Save method must be implemented by subclasses.")

    def load(self, file_path):
        raise NotImplementedError("Load method must be implemented by subclasses.")

