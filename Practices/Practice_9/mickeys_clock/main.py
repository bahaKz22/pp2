import pygame
import datetime
import os

pygame.init()
screen = pygame.display.set_mode((1200, 700))
WHITE = (255, 255, 255)
base = r'/home/user/Documents/bbb/pp2/Practices/Practice_9/mickeys_clock/images'

image_surface = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()
mickey   = pygame.image.load(os.path.join(base, 'mikkey.png')).convert_alpha()
hand_l   = pygame.image.load(os.path.join(base, 'hand_left_centered.png')).convert_alpha()
hand_r   = pygame.image.load(os.path.join(base, 'hand_right_centered.png')).convert_alpha()

resized_image = pygame.transform.scale(image_surface, (800, 600))
res_mickey    = pygame.transform.scale(mickey, (350, 350))
hand_l_base   = pygame.transform.scale(hand_l, (80, 80))
hand_r_base   = pygame.transform.scale(hand_r, (100, 100))

clockc       = (600, 340)
CLOCK_CENTER = (600, 340)

clock = pygame.time.Clock()
done = False

#правильный поворот вокруг основания стрелки
def rotate_hand(image, angle, center):
    rotated = pygame.transform.rotate(image, angle)
    w, h = image.get_size()
    # вектор от основания (низ) до центра повёрнутого изображения
    offset = pygame.math.Vector2(0, -h / 2).rotate(-angle)
    pos = (center[0] + offset.x - rotated.get_width() / 2,
           center[1] + offset.y - rotated.get_height() / 2)
    return rotated, pos

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    m = now.minute
    s = now.second

    minutes_angle = -(m * 6 + s * 0.1)
    seconds_angle = -(s * 6)

    rot_min, pos_min = rotate_hand(hand_r_base, minutes_angle, CLOCK_CENTER)
    rot_sec, pos_sec = rotate_hand(hand_l_base, seconds_angle, CLOCK_CENTER)

    screen.fill(WHITE)
    screen.blit(resized_image, resized_image.get_rect(center=CLOCK_CENTER))
    screen.blit(res_mickey, res_mickey.get_rect(center=clockc))
    screen.blit(rot_min, pos_min)
    screen.blit(rot_sec, pos_sec)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
