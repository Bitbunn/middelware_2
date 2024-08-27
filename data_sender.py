import socket

class DataSender:
    def __init__(self, config):
        self.config = config
        self.seat_ip = self.config["seat"]["ip"]
        self.seat_port = self.config["seat"]["port"]
        self.lighting_ip = self.config["lighting"]["ip"]
        self.lighting_port = self.config["lighting"]["port"]

    def send(self, telemetry_data):
        if telemetry_data is None:
            print("No telemetry data to send.")
            return
        self.send_to_seat(telemetry_data)
        self.send_to_lighting(telemetry_data)

    def send_to_seat(self, telemetry_data):
        print(f"Sending to seat: {telemetry_data}")
        # Add actual sending logic here

    def send_to_lighting(self, telemetry_data):
        print(f"Sending to lighting: {telemetry_data}")
        # Add actual sending logic here
