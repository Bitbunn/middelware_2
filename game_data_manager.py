import threading
from game_data_receiver_factory import GameDataReceiverFactory
from data_sender import DataSender

class GameDataManager: 
    def __init__(self, config):
        self.config = config
        self.receiver = GameDataReceiverFactory.create_receiver(self.config)
        self.sender = DataSender(self.config)
        self.running = False

    def start(self):
        print("Starting GameDataManager...")
        self.receiver.connect()
        self.running = True
        self.receiver_thread = threading.Thread(target=self.receive_data)
        self.sender_thread = threading.Thread(target=self.send_data)
        self.receiver_thread.start()
        self.sender_thread.start()

    def stop(self):
        print("Stopping GameDataManager...")
        self.running = False
        self.receiver_thread.join()
        self.sender_thread.join()

    def receive_data(self):
        while self.running:
            print("Receiving data...")
            self.receiver.receive()
            print(f"Received data: {self.receiver.telemetry_data}")

    def send_data(self):
        while self.running:
            print("Sending data...")
            self.sender.send(self.receiver.telemetry_data)
            print(f"Data sent: {self.receiver.telemetry_data}")
