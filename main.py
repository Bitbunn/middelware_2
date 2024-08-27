import sys
from game_data_manager import GameDataManager
import yaml

def load_config(game_name):
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    if game_name not in config['available_games']:
        raise ValueError(f"Game '{game_name}' not found in available games.")
    config['selected_game'] = config['available_games'][game_name]
    return config

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <game_name>")
        sys.exit(1)

    game_name = sys.argv[1]
    config = load_config(game_name)
    manager = GameDataManager(config)
    try:
        manager.start()
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        manager.stop()
 
