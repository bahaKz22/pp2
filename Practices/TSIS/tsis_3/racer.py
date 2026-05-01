import pygame
import random
import sys
import os
from persistence import load_settings

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Глобальные переменные для изображений, чтобы загрузить их один раз
BG_IMAGE = None
PLAYER_IMAGE = None
ENEMY_IMAGE = None

def load_assets(settings):
    """Глобальная функция загрузки ассетов (изображений и звуков)."""
    global BG_IMAGE, PLAYER_IMAGE, ENEMY_IMAGE
    
    # 1. Загружаем фон и растягиваем его
    img_bg = pygame.image.load("assets/images/street.png")
    BG_IMAGE = pygame.transform.scale(img_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # 2. Загружаем машину врага
    img_e = pygame.image.load("assets/images/car2.png")
    ENEMY_IMAGE = pygame.transform.scale(img_e, (60, 100))

    # 3. Загружаем машину игрока (БЕЗ ФИЛЬТРОВ, чтобы она была нормальной)
    img_p = pygame.image.load("assets/images/car1.png")
    PLAYER_IMAGE = pygame.transform.scale(img_p, (60, 100))
        
    # 4. Загружаем звуки
    if settings["sound"]:
        if os.path.exists("assets/music/background.wav"):
            pygame.mixer.music.load("assets/music/background.wav")
            pygame.mixer.music.play(-1)

# --- КЛАССЫ ИГРОВЫХ ОБЪЕКТОВ ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_IMAGE 
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.shield_active = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 7 
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 7

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed_offset):
        super().__init__()
        self.image = ENEMY_IMAGE 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-150, -50))
        self.speed_offset = speed_offset

    def move(self, global_speed):
        self.rect.y += int(global_speed + self.speed_offset)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        chance = random.randint(1, 10)
        if chance <= 5: 
            self.color = (205, 127, 50); self.r = 10; self.val = 1
        elif chance <= 8: 
            self.color = (192, 192, 192); self.r = 13; self.val = 3
        else: 
            self.color = (255, 215, 0); self.r = 16; self.val = 5

        self.image = pygame.Surface((self.r * 2, self.r * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.r, self.r), self.r)
        pygame.draw.circle(self.image, (255, 255, 255), (self.r - 3, self.r - 3), 3)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), random.randint(-200, -50))

    def move(self, global_speed):
        self.rect.y += int(global_speed / 2 + 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class OilSpill(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 40), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, (30, 30, 30), self.image.get_rect()) 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-200, -50))

    def move(self, global_speed):
        self.rect.y += int(global_speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, p_type):
        super().__init__()
        self.type = p_type
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        r_rect = self.image.get_rect()
        
        if p_type == "Nitro": 
            pygame.draw.polygon(self.image, (0, 255, 255), [(15,0), (0,30), (30,30)]) 
        elif p_type == "Shield": 
            pygame.draw.rect(self.image, (255, 0, 255), r_rect, border_radius=5) 
        elif p_type == "Repair": 
            pygame.draw.circle(self.image, (0, 255, 0), (15,15), 15) 

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -100)

    def move(self, global_speed):
        self.rect.y += int(global_speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# --- ГЛАВНАЯ ФУНКЦИЯ ИГРЫ ---

def play_game(screen):
    clock = pygame.time.Clock()
    settings = load_settings()
    load_assets(settings) 
    
    font = pygame.font.SysFont("Verdana", 20)
    
    # Загружаем звук аварии
    crash_sound = None
    if settings["sound"] and os.path.exists("assets/music/crash.wav"):
        crash_sound = pygame.mixer.Sound("assets/music/crash.wav")

    global_speed = 5 if settings['difficulty'] == 'normal' else 8
    distance = 0
    coins_score = 0
    lives = 1
    FINISH_LINE = 1000 # Дистанция до конца трассы

    p1 = Player()
    enemies = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(p1)

    SPAWN_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_ENEMY, 1700)
    
    SPAWN_OBSTACLE = pygame.USEREVENT + 2
    pygame.time.set_timer(SPAWN_OBSTACLE, 3500)

    SPAWN_COIN = pygame.USEREVENT + 3
    pygame.time.set_timer(SPAWN_COIN, 2500)

    SPAWN_POWERUP = pygame.USEREVENT + 4
    pygame.time.set_timer(SPAWN_POWERUP, 8000)

    active_powerup = None
    powerup_timer = 0

    running = True
    while running:
        dt = clock.tick(60)
        distance += global_speed * 0.05
        
        # Если доехали до финиша, выходим из цикла
        if distance >= FINISH_LINE:
            running = False
            
        current_global_speed = global_speed + (distance // 150)
        
        if active_powerup == "Nitro":
            game_speed = current_global_speed + 5
        else:
            game_speed = current_global_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            if event.type == SPAWN_ENEMY:
                e = Enemy(random.uniform(0.5, 2.5))
                if not pygame.sprite.spritecollideany(e, enemies) and not pygame.sprite.spritecollideany(e, obstacles):
                    enemies.add(e); all_sprites.add(e)

            if event.type == SPAWN_OBSTACLE:
                if random.random() < 0.5: 
                    obs = OilSpill()
                    if not pygame.sprite.spritecollideany(obs, enemies) and not pygame.sprite.spritecollideany(obs, obstacles):
                        obstacles.add(obs); all_sprites.add(obs)

            if event.type == SPAWN_COIN:
                c = Coin()
                if not pygame.sprite.spritecollideany(c, enemies):
                    coins.add(c); all_sprites.add(c)

            if event.type == SPAWN_POWERUP:
                if len(powerups) == 0:
                    p_type = random.choice(["Nitro", "Shield", "Repair"])
                    p = PowerUp(p_type)
                    if not pygame.sprite.spritecollideany(p, enemies):
                        powerups.add(p); all_sprites.add(p)

        screen.blit(BG_IMAGE, (0, 0))

        p1.move()
        for e in enemies: e.move(game_speed)
        for obs in obstacles: obs.move(game_speed)
        for c in coins: c.move(game_speed)
        for p in powerups: p.move(game_speed)

        all_sprites.draw(screen)

        collected_coins = pygame.sprite.spritecollide(p1, coins, True)
        for c in collected_coins:
            coins_score += c.val

        collected_pu = pygame.sprite.spritecollide(p1, powerups, True)
        for p in collected_pu:
            active_powerup = p.type
            if p.type == "Nitro": powerup_timer = pygame.time.get_ticks() + 4000
            elif p.type == "Shield": p1.shield_active = True
            elif p.type == "Repair": lives += 1; active_powerup = None 

        if active_powerup == "Nitro" and pygame.time.get_ticks() > powerup_timer:
            active_powerup = None

        hit_enemy = pygame.sprite.spritecollideany(p1, enemies)
        hit_obs = pygame.sprite.spritecollideany(p1, obstacles)
        
        if hit_enemy or hit_obs:
            if p1.shield_active:
                p1.shield_active = False 
                if hit_enemy: hit_enemy.kill() 
            else:
                lives -= 1
                if hit_enemy: hit_enemy.kill()
                if hit_obs: hit_obs.kill() 
                if lives <= 0:
                    if settings["sound"] and crash_sound:
                        pygame.mixer.music.stop()
                        crash_sound.play()
                    running = False 

        # --- ОТРИСОВКА ИНТЕРФЕЙСА (UI) ---
        final_score = int(distance + (coins_score * 10))
        txt_score = font.render(f"Score: {final_score}", True, (255, 215, 0))
        txt_lives = font.render(f"Lives: {lives}", True, (255, 100, 100))
        
        rem_dist = max(0, FINISH_LINE - int(distance))
        txt_dist = font.render(f"Left: {rem_dist}m", True, (255, 255, 255))
        
        screen.blit(txt_score, (10, 10))
        screen.blit(txt_lives, (10, 40))
        screen.blit(txt_dist, (10, 70))
        
        if p1.shield_active:
            txt_shield = font.render("SHIELD!", True, (255, 0, 255))
            screen.blit(txt_shield, (SCREEN_WIDTH - 110, 10))
            
        if active_powerup == "Nitro":
            seconds_left = (powerup_timer - pygame.time.get_ticks()) // 1000 + 1
            txt_nitro = font.render(f"NITRO: {seconds_left}s", True, (0, 255, 255))
            screen.blit(txt_nitro, (SCREEN_WIDTH - 110, 40))

        pygame.display.flip()

    # Возвращаем 3 значения: очки, дистанцию и монетки
    return final_score, distance, coins_score