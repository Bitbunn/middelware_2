from game_data_receiver_factory import GameDataReceiverFactory
from data_sender import DataSender
import threading

class GameDataManager:
    def __init__(self, config):
        self.config = config
        self.receivers = []
        self.senders = []

    def start(self):
        # Initialize GameDataReceiver and GameDataSender instances
        for feature in self.config.get("features", []):
            receiver = GameDataReceiverFactory.create_receiver(self.config, feature)
            sender = DataSender(receiver)
            self.receivers.append(receiver)
            self.senders.append(sender)

        # Start all receivers and senders
        for receiver in self.receivers:
            threading.Thread(target=receiver.start_receiving).start()

        for sender in self.senders:
            threading.Thread(target=sender.start_sending).start()

    def stop(self):
        for receiver in self.receivers:
            receiver.stop_receiving()
        for sender in self.senders:
            sender.stop_sending()
