import pygame
import sys
import ui
import racer
from persistence import save_leaderboard

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Racer - Advanced")

    while True:
        action = ui.main_menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        if action == "play":
            username = ui.get_username(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            
            playing = True
            while playing:
                # Теперь мы правильно принимаем 3 значения (очки, дистанция, монетки)
                score, distance, coins = racer.play_game(screen)
                
                # Сохраняем результат
                save_leaderboard({"name": username, "score": score, "distance": int(distance)})
                
                # Передаем монетки в экран Game Over
                go_action = ui.game_over_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, score, distance, coins)
                
                if go_action == "menu":
                    playing = False # Выходим в главное меню
                # Если игрок нажал "Retry", цикл продолжится и игра начнется заново
            
        elif action == "settings":
            ui.settings_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            
        elif action == "leaderboard":
            ui.leaderboard_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == "__main__":
    main()