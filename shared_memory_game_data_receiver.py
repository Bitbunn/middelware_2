import mmap
import struct
from game_data_receiver import GameDataReceiver

class SharedMemoryGameDataReceiver(GameDataReceiver):
    def connect(self):
        self.shared_memory_file = self.selected_game["shared_memory_file"]
        print(f"Connected to shared memory file: {self.shared_memory_file}")

    def receive(self):
        with mmap.mmap(-1, 4096, self.shared_memory_file) as mem:
            data = mem.read(4096)
            unpacked_data = struct.unpack(self.telemetry_format, data)
            self.telemetry_data = self.map_telemetry_data(unpacked_data)
            print(f"Received shared memory data: {self.telemetry_data}")

    def map_telemetry_data(self, raw_data):
        return super().map_telemetry_data(raw_data)
 
