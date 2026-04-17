# Geometric drawing - pygame.draw has many shapes besides circles

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Rectangle: (surface, color, (x, y, width, height))
    pygame.draw.rect(screen, red, (50, 50, 200, 100))

    # Rectangle with border only (width parameter = border thickness)
    pygame.draw.rect(screen, green, (300, 50, 200, 100), 3)

    # Circle: (surface, color, center, radius)
    pygame.draw.circle(screen, blue, (150, 300), 60)

    # Ellipse: (surface, color, bounding_rect)
    pygame.draw.ellipse(screen, yellow, (300, 250, 200, 100))

    # Line: (surface, color, start_pos, end_pos, width)
    pygame.draw.line(screen, white, (550, 50), (750, 150), 3)

    # Polygon: (surface, color, list_of_points)
    pygame.draw.polygon(screen, green, [(600, 300), (700, 200), (750, 350)])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()