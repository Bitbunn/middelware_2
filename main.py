import sys
from game_data_manager import GameDataManager
import yaml
import time

def load_config(game_name):
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    if game_name not in config['games']:
        raise ValueError(f"Game '{game_name}' not found in available games.")
    
    # Load the selected game configuration
    config['selected_game'] = config['games'][game_name]
    
    # Read frequency for UDP reception
    if 'frequency' not in config['selected_game']['udp']:
        raise ValueError(f"Frequency not defined for game '{game_name}' in the config.")
    
    return config

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <game_name>")
        sys.exit(1)

    game_name = sys.argv[1]
    config = load_config(game_name)
    manager = GameDataManager(config)
    
    try:
        manager.start()  # Start the GameDataManager
        
        # Keep the main thread alive while the manager is running
        print("GameDataManager is running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)  # Keep sleeping while the manager is running
    
    except KeyboardInterrupt:
        print("Interrupted by user")
    
    finally:
        manager.stop()  # Stop the manager when the program ends
        print("GameDataManager stopped.")
