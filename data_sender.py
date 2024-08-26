import socket
import time

class DataSender:
    def __init__(self, receiver):
        self.receiver = receiver
        self.running = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.target_address = (self.receiver.config['target']['host'], self.receiver.config['target']['port'])

    def start_sending(self):
        self.running = True
        while self.running:
            data = self.receiver.get_data()
            if data:
                self.send_data(data)
            time.sleep(1 / self.receiver.config.get("send_frequency", 10))

    def send_data(self, data):
        # Convert the data to bytes and send via UDP
        data_bytes = self.prepare_data_for_sending(data)
        self.sock.sendto(data_bytes, self.target_address)

    def prepare_data_for_sending(self, data):
        # Example: Convert data to string, then encode it
        return str(data).encode('utf-8')

    def stop_sending(self):
        self.running = False
