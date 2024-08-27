class GameDataReceiver:
    def __init__(self, config):
        self.config = config
        self.receive_frequency = self.config['general'].get("receive_frequency", 10)
        self.selected_game = self.config['selected_game']
        self.telemetry_format = self.selected_game["telemetry_format"]
        self.data_mapping = self.selected_game["data_mapping"]
        self.running = False
        self.telemetry_data = None

    def connect(self):
        print("Connecting to game data source...")
        # This method will be overridden in subclasses

    def receive(self):
        print("Receiving game data...")
        # This method will be overridden in subclasses

    def map_telemetry_data(self, raw_data):
        print(f"Mapping telemetry data: {raw_data}")
        # Implement your mapping logic here
