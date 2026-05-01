import pygame
import json
import sys
from config import *
import db
from game import run_game

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Pro: DB & Powerups")

font_style = pygame.font.SysFont("bahnschrift", 25)
small_font = pygame.font.SysFont("bahnschrift", 18)

def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except:
        return {"snake_color": [0, 255, 0], "grid_on": True, "sound_on": False}

def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f)

def draw_text(text, font, color, x, y):
    msg = font.render(text, True, color)
    screen.blit(msg, [x, y])

def draw_button(text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clicked = False
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            clicked = True
            pygame.time.delay(200) # Простая защита от двойного клика
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    draw_text(text, small_font, BLACK, x + 10, y + 10)
    return clicked

def get_username():
    """Простой экран для ввода имени"""
    username = ""
    active = True
    while active:
        screen.fill(BLUE)
        draw_text("Введите ваше имя:", font_style, WHITE, WIDTH//2 - 100, HEIGHT//3)
        draw_text(username + "_", font_style, GOLD, WIDTH//2 - 100, HEIGHT//2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username.strip():
                    return username.strip()
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if len(username) < 15:
                        username += event.unicode

def leaderboard_screen():
    running = True
    top_scores = db.get_top_10()
    
    while running:
        screen.fill(BLUE)
        draw_text("ТАБЛИЦА ЛИДЕРОВ", font_style, GOLD, 200, 30)
        
        y_offset = 80
        for i, (usr, sc, lvl, dt) in enumerate(top_scores):
            text = f"{i+1}. {usr} - Счет: {sc} (Ур: {lvl}) [{dt}]"
            draw_text(text, small_font, WHITE, 50, y_offset)
            y_offset += 25
            
        if draw_button("Назад", 250, 340, 100, 40, WHITE, GRAY, True):
            running = False

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

def settings_screen(settings):
    running = True
    colors = {"Зеленый": GREEN, "Фиолетовый": (128, 0, 128), "Желтый": GOLD}
    
    while running:
        screen.fill(BLUE)
        draw_text("НАСТРОЙКИ", font_style, GOLD, 230, 30)
        
        draw_text(f"Сетка: {'ВКЛ' if settings['grid_on'] else 'ВЫКЛ'}", font_style, WHITE, 100, 100)
        if draw_button("Переключить", 350, 95, 120, 30, WHITE, GRAY, True):
            settings['grid_on'] = not settings['grid_on']

        draw_text("Цвет змеи:", font_style, WHITE, 100, 150)
        if draw_button("Зеленый", 250, 150, 80, 30, GREEN, WHITE, True): settings['snake_color'] = GREEN
        if draw_button("Фиол.", 340, 150, 80, 30, (128,0,128), WHITE, True): settings['snake_color'] = (128,0,128)
        
        if draw_button("Сохранить и Назад", 200, 300, 200, 40, WHITE, GRAY, True):
            save_settings(settings)
            running = False

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

def game_over_screen(score, level, pb):
    running = True
    while running:
        screen.fill(BLACK)
        draw_text("ИГРА ОКОНЧЕНА", font_style, RED, 200, 100)
        draw_text(f"Счет: {score}", font_style, WHITE, 250, 150)
        draw_text(f"Уровень: {level}", font_style, WHITE, 250, 180)
        draw_text(f"Рекорд: {max(score, pb)}", font_style, GOLD, 250, 210)
        
        if draw_button("Заново", 150, 280, 120, 40, WHITE, GRAY, True): return True
        if draw_button("В Меню", 330, 280, 120, 40, WHITE, GRAY, True): return False
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

def main_menu():
    db.init_db()
    settings = load_settings()
    
    # Запрашиваем имя один раз при запуске
    username = get_username()
    player_id = db.get_or_create_player(username)

    while True:
        screen.fill(BLUE)
        draw_text(f"Привет, {username}!", font_style, GOLD, 20, 20)
        draw_text("SNAKE PRO", pygame.font.SysFont("bahnschrift", 50), WHITE, 170, 80)
        
        if draw_button("Играть", 240, 160, 120, 40, WHITE, GREEN, True):
            play_again = True
            while play_again:
                score, level = run_game(screen, font_style, player_id, settings)
                pb = db.get_personal_best(player_id)
                play_again = game_over_screen(score, level, pb)

        if draw_button("Лидеры", 240, 215, 120, 40, WHITE, GRAY, True):
            leaderboard_screen()
            
        if draw_button("Настройки", 240, 270, 120, 40, WHITE, GRAY, True):
            settings_screen(settings)
            
        if draw_button("Выход", 240, 325, 120, 40, WHITE, RED, True):
            pygame.quit(); sys.exit()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

if __name__ == "__main__":
    main_menu()