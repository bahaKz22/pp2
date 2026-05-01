import pygame
import random
import time
from config import *
import db

def get_random_pos(exclude_list):
    """Генерация координат, исключая занятые позиции"""
    while True:
        x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * BLOCK_SIZE
        y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * BLOCK_SIZE
        if [x, y] not in exclude_list:
            return [x, y]

def generate_obstacles(level):
    """Генерация препятствий, начиная с 3 уровня"""
    obstacles = []
    if level < 3: return obstacles
    
    num_blocks = min(5 + (level - 3) * 3, 40) # Увеличиваем сложность
    center_safe_zone = [[WIDTH//2 + dx*BLOCK_SIZE, HEIGHT//2 + dy*BLOCK_SIZE] 
                        for dx in range(-3, 4) for dy in range(-3, 4)]
    
    for _ in range(num_blocks):
        while True:
            obs_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / float(BLOCK_SIZE)) * BLOCK_SIZE
            obs_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / float(BLOCK_SIZE)) * BLOCK_SIZE
            
            if [obs_x, obs_y] not in center_safe_zone and [obs_x, obs_y] not in obstacles:
                obstacles.append([obs_x, obs_y])
                break
    return obstacles

def run_game(screen, font_style, player_id, settings):
    clock = pygame.time.Clock()
    
    # Состояние змеи
    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Length_of_snake = 3
    
    # Метрики
    score = 0
    level = 1
    base_speed = 10
    current_speed = base_speed
    personal_best = db.get_personal_best(player_id)
    
    # Объекты на карте
    obstacles = generate_obstacles(level)
    def get_safe_pos():
        return get_random_pos(snake_List + obstacles)

    food_pos = get_safe_pos()
    poison_pos = get_safe_pos() if random.random() > 0.5 else None
    
    # Бонусы
    powerup = None # {'type': 'speed'/'slow'/'shield', 'pos': [x,y], 'spawn_time': 0}
    active_effect = None
    effect_end_time = 0
    has_shield = False

    game_over = False

    while not game_over:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return score, level
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change, y1_change = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change, y1_change = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change, y1_change = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change, y1_change = 0, BLOCK_SIZE

        # Логика эффектов бонусов
        if active_effect and current_time > effect_end_time:
            active_effect = None
            current_speed = base_speed
        
        if active_effect == "speed": current_speed = base_speed + 8
        elif active_effect == "slow": current_speed = max(5, base_speed - 5)
        else: current_speed = base_speed

        # Логика спавна бонусов (раз в некоторое время)
        if powerup is None and random.randint(1, 100) == 1:
            ptype = random.choice(["speed", "slow", "shield"])
            powerup = {'type': ptype, 'pos': get_safe_pos(), 'spawn_time': current_time}
        
        # Исчезновение несобранного бонуса (через 8 сек)
        if powerup and current_time - powerup['spawn_time'] > 8000:
            powerup = None

        # Движение
        x1 += x1_change
        y1 += y1_change
        snake_Head = [x1, y1]

        # --- Проверка столкновений ---
        # --- Проверка столкновений ---
        hit_wall = x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0
        hit_obstacle = snake_Head in obstacles
        
        # Проверяем самопересечение, только если змея уже начала движение
        is_moving = (x1_change != 0 or y1_change != 0)
        hit_self = is_moving and (snake_Head in snake_List[:-1])

        if hit_wall or hit_obstacle or hit_self:
            if has_shield:
                has_shield = False
                # Игнорируем урон 1 раз
                if hit_wall: # Сквозной проход через стену
                    if x1 >= WIDTH: x1 = 0
                    elif x1 < 0: x1 = WIDTH - BLOCK_SIZE
                    elif y1 >= HEIGHT: y1 = 0
                    elif y1 < 0: y1 = HEIGHT - BLOCK_SIZE
                    snake_Head = [x1, y1]
            else:
                db.save_session(player_id, score, level)
                return score, level # Конец игры

        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Отрисовка
        screen.fill(BLUE)
        if settings.get("grid_on", True):
            for x in range(0, WIDTH, BLOCK_SIZE): pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, BLOCK_SIZE): pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

        # Отрисовка препятствий
        for obs in obstacles:
            pygame.draw.rect(screen, GRAY, [obs[0], obs[1], BLOCK_SIZE, BLOCK_SIZE])

        # Отрисовка еды, яда и бонуса
        pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])
        if poison_pos:
            pygame.draw.rect(screen, DARK_RED, [poison_pos[0], poison_pos[1], BLOCK_SIZE, BLOCK_SIZE])
        if powerup:
            color = COLOR_SPEED if powerup['type'] == 'speed' else COLOR_SLOW if powerup['type'] == 'slow' else COLOR_SHIELD
            pygame.draw.rect(screen, color, [powerup['pos'][0], powerup['pos'][1], BLOCK_SIZE, BLOCK_SIZE])

        # Отрисовка змеи
        snake_color = tuple(settings.get("snake_color", GREEN))
        for i, segment in enumerate(snake_List):
            color = snake_color
            if has_shield and i == len(snake_List)-1: # Голова светится если есть щит
                color = COLOR_SHIELD 
            pygame.draw.rect(screen, color, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        # Поедание обычной еды
        if snake_Head == food_pos:
            Length_of_snake += 1
            score += 1
            food_pos = get_safe_pos()
            if random.random() > 0.3: # 70% шанс появления яда
                poison_pos = get_safe_pos()
            
            new_level = (score // 3) + 1
            if new_level > level:
                level = new_level
                base_speed += 2
                obstacles = generate_obstacles(level) # Обновляем препятствия

        # Поедание яда
        if poison_pos and snake_Head == poison_pos:
            Length_of_snake -= 2
            poison_pos = None
            if Length_of_snake <= 1:
                db.save_session(player_id, score, level)
                return score, level # Умер от яда
            snake_List = snake_List[-Length_of_snake:] # Отрезаем хвост

        # Подбор бонуса
        if powerup and snake_Head == powerup['pos']:
            if powerup['type'] == 'shield':
                has_shield = True
            else:
                active_effect = powerup['type']
                effect_end_time = current_time + 5000 # 5 секунд
            powerup = None

        # Интерфейс поверх игры
        score_msg = font_style.render(f"Счет: {score} | Уровень: {level} | Рекорд: {personal_best}", True, WHITE)
        screen.blit(score_msg, [10, 10])

        pygame.display.update()
        clock.tick(current_speed)