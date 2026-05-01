import pygame
import sys
import random
import time

pygame.init()

# настройки экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# шрифты для текста
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# стартовые переменные
speed = 5
score = 0
coins = 0

# загружаем фон и растягиваем его на весь экран
bg = pygame.image.load("images/street.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# включаем музыку на фон (играет бесконечно)
pygame.mixer.music.load("music/background.wav")
pygame.mixer.music.play(-1)

# класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("images/car1.png")
        self.image = pygame.transform.scale(img, (60, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) # ставим машину внизу

    def move(self):
        keys = pygame.key.get_pressed()
        # едем влево или вправо, если не уперлись в край экрана
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

# класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("images/car2.png")
        self.image = pygame.transform.scale(img, (60, 100))
        self.rect = self.image.get_rect()
        # появляемся сверху в случайном месте
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global score
        self.rect.y += int(speed)
        # если враг уехал за нижний край экрана
        if self.rect.top > SCREEN_HEIGHT:
            score += 1 # даем очко
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) # возвращаем наверх

# класс монетки
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # случайно выбираем какую монетку сделать (1 до 10)
        chance = random.randint(1, 10)
        if chance <= 5:
            # бронза (чаще всего)
            self.color = (205, 127, 50) 
            self.r = 10
            self.val = 1
        elif chance <= 8:
            # серебро
            self.color = (192, 192, 192) 
            self.r = 13
            self.val = 3
        else:
            # золото (редко)
            self.color = (255, 215, 0) 
            self.r = 16
            self.val = 5

        # рисуем круглую монетку
        self.image = pygame.Surface((self.r * 2, self.r * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.r, self.r), self.r)
        pygame.draw.circle(self.image, (255, 255, 255), (self.r - 3, self.r - 3), 3) # блик
        
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)

    def move(self):
        # монетки падают чуть медленнее машин
        coin_speed = speed / 2
        if coin_speed < 3:
            coin_speed = 3
        self.rect.y += int(coin_speed)

        # удаляем если улетела вниз
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# создаем объекты машин
p1 = Player()
e1 = Enemy()

# создаем группы (чтобы было легко рисовать и проверять столкновения)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)

enemies_group = pygame.sprite.Group()
enemies_group.add(e1)

coins_group = pygame.sprite.Group()

# таймер для создания монеток (каждые 2.5 секунды)
SPAWN_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_COIN, 2500)

# главный цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # если сработал таймер - создаем монетку
        if event.type == SPAWN_COIN:
            new_coin = Coin()
            coins_group.add(new_coin)
            all_sprites.add(new_coin)

    # рисуем фон
    screen.blit(bg, (0, 0))

    # двигаем и рисуем все машины и монетки
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.move()

    # собираем монетки
    prev_coins = coins
    collected_coins = pygame.sprite.spritecollide(p1, coins_group, True)
    for c in collected_coins:
        coins += c.val
    
    # ускоряем игру если собрали достаточно монеток (каждые 5 веса)
    if coins // 5 > prev_coins // 5:
        speed += 0.5 * (coins // 5 - prev_coins // 5)

    # пишем текст статистики слева сверху
    text_score = font_small.render("Score: " + str(score), True, (255, 215, 0))
    text_coins = font_small.render("Coins: " + str(coins), True, (255, 215, 0))
    text_speed = font_small.render("Speed: " + str(speed), True, (255, 215, 0))
    
    screen.blit(text_score, (10, 10))
    screen.blit(text_coins, (10, 35))
    screen.blit(text_speed, (10, 60))

    # если машина врезалась во врага
    if pygame.sprite.spritecollideany(p1, enemies_group):
        pygame.mixer.music.stop()
        
        # звук аварии
        crash_sound = pygame.mixer.Sound("music/crash.wav")
        crash_sound.play()
        
        # делаем красный экран
        screen.fill((255, 0, 0))
        
        # выводим текст проигрыша
        game_over_text = font_big.render("GAME OVER", True, (0, 0, 0))
        score_text = font_small.render("Score: " + str(score), True, (0, 0, 0))
        coins_text = font_small.render("Coins: " + str(coins), True, (0, 0, 0))
        
        # ставим текст по центру
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 120))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 230))
        screen.blit(coins_text, (SCREEN_WIDTH // 2 - coins_text.get_width() // 2, 280))
        
        pygame.display.update()
        time.sleep(4) # ждем 4 секунды
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60) # 60 кадров в секунду