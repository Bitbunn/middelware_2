from udp_game_data_receiver import UDPGameDataReceiver
from shared_memory_game_data_receiver import SharedMemoryGameDataReceiver

class GameDataReceiverFactory:
    @staticmethod
    def create_receiver(config, feature):
        if config['protocol'] == 'udp':
            return UDPGameDataReceiver(config, feature)
        elif config['protocol'] == 'shared_memory':
            return SharedMemoryGameDataReceiver(config, feature)
        else:
            raise ValueError("Unsupported protocol")
