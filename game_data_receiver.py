from abc import ABC, abstractmethod

class GameDataReceiver(ABC):
    def __init__(self, config, feature):
        self.config = config
        self.feature = feature
        self.running = False
        self.data = {}

    @abstractmethod
    def start_receiving(self):
        pass

    def stop_receiving(self):
        self.running = False

    def update_data(self, data):
        self.data.update(data)

    def get_data(self):
        return self.data
