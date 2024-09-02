import time
import threading

class GameDataManager:
    def __init__(self, config):
        self.config = config
        self.selected_game = config['selected_game']
        self.receiver = self.create_receiver()  # Assume a method that creates the receiver
        self.sender = self.create_sender()  # Assume a method that creates the sender
        self.running = False
    
    def start(self):
        print("Starting GameDataManager...")
        self.receiver.connect()
        self.running = True
        print("GameDataManager running:", self.running)
        
        # Start threads for receiving and sending data
        self.receiver_thread = threading.Thread(target=self.receive_data)
        self.sender_thread = threading.Thread(target=self.send_data)
        self.receiver_thread.start()
        self.sender_thread.start()

    def stop(self):
        print("Stopping GameDataManager...")
        self.running = False
        print("self.running set to False in stop() method.")
        
        # Ensure threads are started before trying to join them
        if hasattr(self, 'receiver_thread') and self.receiver_thread.is_alive():
            self.receiver_thread.join()
        if hasattr(self, 'sender_thread') and self.sender_thread.is_alive():
            self.sender_thread.join()
        print("GameDataManager stopped successfully.")

    def receive_data(self):
        retry_count = 0
        
        # Use frequency from configuration
        frequency = self.selected_game['udp']['frequency']  # Get frequency from config
        
        while self.running:
            try:
                print("Receiving data...")
                self.receiver.receive()  # Attempt to receive data
                print(f"Data received: {self.receiver.telemetry_data}")  # Log received data
                retry_count = 0  # Reset retry count after successful operation

                # Sleep to control the frequency of reception using the config value
                time.sleep(frequency)  # Sleep to maintain the desired frequency

            except Exception as e:
                print(f"Error receiving data: {e}")  # Log any errors encountered
                retry_count += 1
                if retry_count >= 3:  # Allow a few retries before stopping
                    print("Max retries reached in receive_data. Setting self.running to False.")
                    self.running = False  # Set running to False due to max retries
                    break  # Exit the loop
            
            print(f"End of receive_data loop. self.running: {self.running}")
        print("Exiting receive_data thread...")  # Log when the thread exits

    def send_data(self):
        retry_count = 0
        while self.running:
            try:
                print("Sending data...")
                telemetry_data = self.receiver.telemetry_data  # Fetch the latest telemetry data
                if telemetry_data:  # Only send if telemetry data is not None or empty
                    self.sender.send(telemetry_data)
                    print(f"Data sent: {telemetry_data}")
                    retry_count = 0  # Reset retry count after successful send
                else:
                    print("No valid telemetry data to send.")
                
                # You may add a sleep here to control send frequency if needed

            except Exception as e:
                print(f"Error sending data: {e}")  # Log any errors encountered
                retry_count += 1
                if retry_count >= 3:  # Allow a few retries before stopping
                    print("Max retries reached in send_data. Setting self.running to False.")
                    self.running = False  # Set running to False due to max retries
                    break  # Exit the loop
            
            print(f"End of send_data loop. self.running: {self.running}")
        print("Exiting send_data thread...")  # Log when the thread exits
    
    # Assuming methods to create receiver and sender
    def create_receiver(self):
        # Code to create and return a receiver object
        pass
    
    def create_sender(self):
        # Code to create and return a sender object
        pass
