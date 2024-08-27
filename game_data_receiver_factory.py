from udp_game_data_receiver import UDPGameDataReceiver
from shared_memory_game_data_receiver import SharedMemoryGameDataReceiver

class GameDataReceiverFactory:
    @staticmethod
    def create_receiver(config):
        protocol = config['selected_game']['protocol']
        if protocol == 'udp':
            return UDPGameDataReceiver(config)
        elif protocol == 'shared_memory':
            return SharedMemoryGameDataReceiver(config)
        else:
            raise ValueError(f"Unsupported protocol: {protocol}")
