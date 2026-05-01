# Snake Pro: Database Integration & Advanced Gameplay (TSIS 4)

This is an extended version of the classic "Snake" game, written in Python using the **Pygame** library. This version introduces **PostgreSQL** database integration for persistent leaderboards, alongside new gameplay mechanics: power-ups, poison, obstacles, and disappearing food.

## 🌟 Features

* **Database & Leaderboard:** The game saves player results in a PostgreSQL database. You can view the Top 10 all-time players in the Main Menu, and your personal best is displayed during gameplay.
* **Various Food Types:**
  * 🍎 *Red Food* — regular food (+1 score, +1 length).
  * 🟡 *Golden Food* — appears rarely and disappears after 5 seconds (+3 score, +1 length).
  * 🟤 *Poison (Dark Red)* — shortens the snake by 2 segments. If the length drops to 1 or less, it's Game Over.
* **Power-ups:** Spawn on the field for 8 seconds. The effect lasts for 5 seconds after collection:
  * ⚡ *Blue Block (Speed)* — increases snake speed.
  * 🐢 *Orange Block (Slow)* — decreases snake speed.
  * 🛡️ *Silver Block (Shield)* — grants immunity to a single collision (allows passing through a wall or obstacle once).
* **Obstacles:** Starting from Level 3, gray wall blocks appear on the map. The number of blocks increases with each level.
* **Settings System:** You can toggle the grid on/off or change the snake's color in the Main Menu. Settings are saved locally in a `settings.json` file.

## 🛠️ Project Structure

* `main.py` — Entry point, handles the main menu, game over, and settings screens.
* `game.py` — Core game logic (movement, collisions, spawning food and power-ups).
* `db.py` — PostgreSQL connection and table management functions.
* `config.py` — Constants (colors, screen size, base settings).
* `settings.json` — Local file for saving user preferences (auto-generated).
