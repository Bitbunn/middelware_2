import sys
import yaml
import time
from game_data_manager import GameDataManager

def load_config(game_name):
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    # Check if the game name is in the available games
    if game_name not in config['available_games']:
        raise ValueError(f"Game '{game_name}' not found in available games. Available games: {list(config['available_games'].keys())}")

    # Set the selected game
    config['selected_game'] = config['available_games'][game_name]
    return config

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the name of the game as a command-line argument.")
        sys.exit(1)

    game_name = sys.argv[1]
    config = load_config(game_name)

    # Initialize and start the game data manager
    manager = GameDataManager(config)
    manager.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        manager.stop()
