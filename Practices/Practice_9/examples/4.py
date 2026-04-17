import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
COLOR_GREEN = (0,255,0)
running = True
is_red = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red
        
    if is_red:
        screen.fill(COLOR_GREEN)
    else:
        screen.fill(COLOR_BLUE)

    

    pygame.draw.circle(screen, COLOR_RED, (100,100), 40)
    pygame.display.flip()