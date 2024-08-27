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
        telemetry_data = {
            "vehicle_pos": [raw_data[self.data_mapping["vehicle_pos"][i]] for i in range(3)],
            "vehicle_speed": [raw_data[self.data_mapping["vehicle_speed"][i]] for i in range(3)],
            "vehicle_accel": [raw_data[self.data_mapping["vehicle_accel"][i]] for i in range(3)],
            "vehicle_ang_euler": [raw_data[self.data_mapping["vehicle_ang_euler"][i]] for i in range(3)],
            "vehicle_ang_speed": [raw_data[self.data_mapping["vehicle_ang_speed"][i]] for i in range(3)],
            "engine_rpm": raw_data[self.data_mapping["engine_rpm"]],
            "susp_deflect": [raw_data[self.data_mapping["susp_deflect"][i]] for i in range(4)],
        }
        print(f"Mapped telemetry data: {telemetry_data}")
        return telemetry_data
