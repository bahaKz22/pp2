import json
import os

SETTINGS_FILE = 'settings.json'
LEADERBOARD_FILE = 'leaderboard.json'

def load_settings():
    default_settings = {"sound": True, "car_color": "red", "difficulty": "normal"}
    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
        return default_settings
    
    # Добавлена защита от пустого/сломанного файла
    try:
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        save_settings(default_settings)
        return default_settings

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    
    # Добавлена защита от пустого/сломанного файла
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_leaderboard(score_entry):
    board = load_leaderboard()
    board.append(score_entry)
    board = sorted(board, key=lambda x: x['score'], reverse=True)[:10]
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(board, f, indent=4)