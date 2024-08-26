import time
import mmap
from game_data_receiver import GameDataReceiver

class SharedMemoryGameDataReceiver(GameDataReceiver):
    def __init__(self, config, feature):
        super().__init__(config, feature)
        # Initialize shared memory access here
        self.shared_mem = mmap.mmap(-1, config['shared_memory']['size'], config['shared_memory']['name'])

    def start_receiving(self):
        self.running = True
        while self.running:
            self.shared_mem.seek(0)
            data = self.shared_mem.read(self.config['shared_memory']['size'])
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
