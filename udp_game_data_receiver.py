import socket
import time
from game_data_receiver import GameDataReceiver

class UDPGameDataReceiver(GameDataReceiver):
    def __init__(self, config, feature):
        super().__init__(config, feature)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((config['udp']['host'], config['udp']['port']))

    def start_receiving(self):
        self.running = True
        while self.running:
            data, _ = self.sock.recvfrom(1024)  # Buffer size
            parsed_data = self.map_telemetry_data(data)
            self.update_data(parsed_data)
            time.sleep(1 / self.config.get("receive_frequency", 10))

    def map_telemetry_data(self, raw_data):
        # Implement your mapping logic here
        telemetry_format = self.config['telemetry_format']
        unpacked_data = struct.unpack(telemetry_format, raw_data)

        mapped_data = {}
        for key, indices in self.config['data_mapping'].items():
            if isinstance(indices, list):
                mapped_data[key] = [unpacked_data[i] for i in indices]
            else:
                mapped_data[key] = unpacked_data[indices]

        return mapped_data
