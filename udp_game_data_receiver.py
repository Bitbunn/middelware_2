import socket
import struct
from game_data_receiver import GameDataReceiver

class UDPGameDataReceiver(GameDataReceiver):
    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.selected_game["ip"], self.selected_game["port"]))
        print(f"Connected to UDP {self.selected_game['ip']}:{self.selected_game['port']}")

    def receive(self):
        data, _ = self.sock.recvfrom(self.selected_game["buffer_size"])
        unpacked_data = struct.unpack(self.telemetry_format, data)
        self.telemetry_data = self.map_telemetry_data(unpacked_data)
        print(f"Received UDP data: {self.telemetry_data}")

    def map_telemetry_data(self, raw_data):
        return super().map_telemetry_data(raw_data)
 
