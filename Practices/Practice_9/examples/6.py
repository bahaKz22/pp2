import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

COLOR_RED = (255,0,0)
COLOR_GREEN = (0,255,0)
COLOR_BLUE = (0,0,255)

circle_x = WIDTH//2
circle_y = HEIGHT//2

running = True
is_red = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red

            if event.key == pygame.K_UP:
                circle_y -= 10
            if event.key == pygame.K_DOWN:
                circle_y += 10
            if event.key == pygame.K_RIGHT:
                circle_x += 10
            if event.key == pygame.K_LEFT:
                circle_x -= 10


    if is_red:
        screen.fill(COLOR_BLUE)
        pygame.draw.circle(screen, COLOR_GREEN, (circle_x,circle_y), 40)
    else:
        screen.fill(COLOR_GREEN)
        pygame.draw.circle(screen, COLOR_RED, (circle_x,circle_y), 40)
    
    pygame.display.flip()