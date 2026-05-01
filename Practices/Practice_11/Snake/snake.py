import pygame
import random
import time

# --- Инициализация Pygame ---
pygame.init()

# --- Настройки экрана и игры ---
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20 # Размер одного блока змеи и еды
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# --- Цвета (RGB) ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)       # Обычная еда
GREEN = (0, 255, 0)       # Цвет змеи
BLUE = (50, 153, 213)     # Фон экрана
GOLD = (255, 215, 0)      # Специальная еда (исчезающая)
GRID_COLOR = (40, 130, 190) # Цвет сетки (немного темнее фона)

# --- Настройки шрифта для счетчиков ---
font_style = pygame.font.SysFont("bahnschrift", 20)

def draw_text(text, color, x, y):
    """Функция для вывода текста на экран"""
    msg = font_style.render(text, True, color)
    screen.blit(msg, [x, y])

def get_random_food_pos(snake_list):
    """
    Генерирует случайные координаты для еды.
    Проверяет, чтобы еда не появилась на стене или внутри самой змеи.
    """
    while True:
        food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * BLOCK_SIZE
        food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * BLOCK_SIZE
        
        if [food_x, food_y] not in snake_list:
            return [food_x, food_y]

def gameLoop():
    """Основной игровой цикл"""
    game_over = False
    game_close = False

    # Начальные координаты змеи (центр экрана)
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Изменение координат при движении
    x1_change = 0
    y1_change = 0

    # Тело змеи
    snake_List = []
    Length_of_snake = 1

    # --- Игровые метрики ---
    score = 0
    level = 1
    base_speed = 10
    current_speed = base_speed

    # --- Настройки обычной еды (Вес = 1) ---
    food_pos = get_random_food_pos(snake_List)
    food_weight = 1

    # --- Настройки специальной еды (Вес = 3, Таймер) ---
    special_food_pos = None
    special_food_spawn_time = 0
    special_food_duration = 5000 # Время жизни в миллисекундах (5 секунд)

    clock = pygame.time.Clock()

    while not game_over:

        # Экран проигрыша
        while game_close == True:
            screen.fill(BLACK)
            draw_text(f"Игра окончена! Ваш счет: {score}. Нажмите Q-Выход или C-Заново", RED, WIDTH / 10, HEIGHT / 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop() # Перезапуск игры

        # Обработка нажатий клавиш пользователя
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # --- Проверка столкновения со стенами (Границы) ---
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Обновление координат головы
        x1 += x1_change
        y1 += y1_change
        
        # 1. Заливаем фон
        screen.fill(BLUE)

        # 2. Отрисовка сетки (добавляем поверх фона, но под змею и еду)
        for x in range(0, WIDTH, BLOCK_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, BLOCK_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

        # --- Логика исчезающей еды (Таймер) ---
        current_time = pygame.time.get_ticks()
        
        if special_food_pos is None and random.randint(1, 150) == 1:
            special_food_pos = get_random_food_pos(snake_List)
            special_food_spawn_time = current_time

        if special_food_pos is not None:
            if current_time - special_food_spawn_time > special_food_duration:
                special_food_pos = None

        # --- Отрисовка еды ---
        pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])
        
        if special_food_pos is not None:
            pygame.draw.rect(screen, GOLD, [special_food_pos[0], special_food_pos[1], BLOCK_SIZE, BLOCK_SIZE])

        # --- Обновление тела змеи ---
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(screen, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

        # --- Вывод счета и уровня (Счетчик) ---
        draw_text(f"Счет: {score}   Уровень: {level}", WHITE, 10, 10)

        pygame.display.update()

        # --- Логика поедания обычной еды ---
        if x1 == food_pos[0] and y1 == food_pos[1]:
            food_pos = get_random_food_pos(snake_List)
            Length_of_snake += 1
            score += food_weight
            
            new_level = (score // 3) + 1
            if new_level > level:
                level = new_level
                current_speed += 2

        # --- Логика поедания специальной еды ---
        if special_food_pos is not None and x1 == special_food_pos[0] and y1 == special_food_pos[1]:
            special_food_pos = None
            Length_of_snake += 1
            score += 3
            
            new_level = (score // 3) + 1
            if new_level > level:
                level = new_level
                current_speed += 2

        clock.tick(current_speed)

    pygame.quit()
    quit()

# Запуск игры
if __name__ == "__main__":
    gameLoop()