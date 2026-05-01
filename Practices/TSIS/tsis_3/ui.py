import pygame
import sys
from persistence import load_settings, save_settings, load_leaderboard

pygame.init()
font_big = pygame.font.SysFont("Verdana", 50)
font_small = pygame.font.SysFont("Verdana", 25)

class Button:
    def __init__(self, text, x, y, w, h, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, current_color, self.rect, border_radius=10)
        text_surf = font_small.render(self.text, True, (255, 255, 255))
        screen.blit(text_surf, (self.rect.centerx - text_surf.get_width()//2, self.rect.centery - text_surf.get_height()//2))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

def get_username(screen, width, height):
    name = ""
    running = True
    while running:
        screen.fill((30, 30, 30))
        title = font_big.render("Enter Username:", True, (255, 255, 255))
        name_surf = font_big.render(name + "_", True, (0, 255, 0))
        
        screen.blit(title, (width//2 - title.get_width()//2, 150))
        screen.blit(name_surf, (width//2 - name_surf.get_width()//2, 250))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name != "":
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 10 and event.unicode.isalnum():
                    name += event.unicode
                    
        pygame.display.flip()

def main_menu(screen, width, height):
    btn_play = Button("Play", width//2 - 100, 200, 200, 50, (0, 150, 0), (0, 200, 0))
    btn_lb = Button("Leaderboard", width//2 - 100, 270, 200, 50, (0, 0, 150), (0, 0, 200))
    btn_set = Button("Settings", width//2 - 100, 340, 200, 50, (150, 100, 0), (200, 150, 0))
    btn_quit = Button("Quit", width//2 - 100, 410, 200, 50, (150, 0, 0), (200, 0, 0))

    while True:
        screen.fill((30, 30, 30))
        title = font_big.render("RACER", True, (255, 215, 0))
        screen.blit(title, (width//2 - title.get_width()//2, 80))

        for btn in [btn_play, btn_lb, btn_set, btn_quit]:
            btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if btn_play.is_clicked(event): return "play"
            if btn_lb.is_clicked(event): return "leaderboard"
            if btn_set.is_clicked(event): return "settings"
            if btn_quit.is_clicked(event):
                pygame.quit()
                sys.exit()
                
        pygame.display.flip()

def settings_screen(screen, width, height):
    settings = load_settings()
    btn_sound = Button(f"Sound: {'ON' if settings['sound'] else 'OFF'}", width//2 - 100, 150, 200, 50, (100, 100, 100), (150, 150, 150))
    btn_diff = Button(f"Diff: {settings['difficulty']}", width//2 - 100, 220, 200, 50, (100, 100, 100), (150, 150, 150))
    btn_back = Button("Back", width//2 - 100, 360, 200, 50, (150, 0, 0), (200, 0, 0))

    while True:
        screen.fill((30, 30, 30))
        for btn in [btn_sound, btn_diff, btn_back]:
            btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if btn_back.is_clicked(event):
                save_settings(settings)
                return
            if btn_sound.is_clicked(event):
                settings['sound'] = not settings['sound']
                btn_sound.text = f"Sound: {'ON' if settings['sound'] else 'OFF'}"
            if btn_diff.is_clicked(event):
                settings['difficulty'] = "hard" if settings['difficulty'] == "normal" else "normal"
                btn_diff.text = f"Diff: {settings['difficulty']}"
                
        pygame.display.flip()

def leaderboard_screen(screen, width, height):
    board = load_leaderboard()
    btn_back = Button("Back", width//2 - 100, 500, 200, 50, (150, 0, 0), (200, 0, 0))

    while True:
        screen.fill((30, 30, 30))
        title = font_big.render("TOP 10", True, (255, 215, 0))
        screen.blit(title, (width//2 - title.get_width()//2, 30))

        y = 100
        for i, entry in enumerate(board):
            txt = font_small.render(f"{i+1}. {entry['name']} - {entry['score']}", True, (255, 255, 255))
            screen.blit(txt, (50, y))
            y += 35

        btn_back.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if btn_back.is_clicked(event):
                return
        pygame.display.flip()

# Здесь мы принимаем coins как новый аргумент
def game_over_screen(screen, width, height, score, distance, coins):
    btn_retry = Button("Retry", width//2 - 100, 350, 200, 50, (0, 100, 150), (0, 150, 200))
    btn_menu = Button("Main Menu", width//2 - 100, 420, 200, 50, (0, 150, 0), (0, 200, 0))
    
    while True:
        screen.fill((200, 0, 0))
        title = font_big.render("GAME OVER", True, (0, 0, 0))
        score_t = font_small.render(f"Score: {score}", True, (255, 255, 255))
        dist_t = font_small.render(f"Distance: {int(distance)}m", True, (255, 255, 255))
        coins_t = font_small.render(f"Coins: {coins}", True, (255, 215, 0))
        
        screen.blit(title, (width//2 - title.get_width()//2, 80))
        screen.blit(score_t, (width//2 - score_t.get_width()//2, 170))
        screen.blit(dist_t, (width//2 - dist_t.get_width()//2, 220))
        screen.blit(coins_t, (width//2 - coins_t.get_width()//2, 270))
        
        btn_retry.draw(screen)
        btn_menu.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if btn_retry.is_clicked(event):
                return "retry"
            if btn_menu.is_clicked(event):
                return "menu"
        pygame.display.flip()