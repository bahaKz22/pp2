import pygame
import sys
from datetime import datetime
from tools import flood_fill, draw_shape  # Импортируем наши функции из tools.py

# Константы
WIDTH, HEIGHT = 900, 700
TOOLBAR_HEIGHT = 80
FPS = 60

# Цвета
COLORS = {
    "Black": (0, 0, 0), "White": (255, 255, 255), "Red": (255, 0, 0),
    "Green": (0, 255, 0), "Blue": (0, 0, 255), "Yellow": (255, 255, 0)
}
BG_COLOR = (240, 240, 240)

class PaintApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("TSIS 2: Pygame Paint")
        self.clock = pygame.time.Clock()

        # Поверхности
        self.canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
        self.canvas.fill(COLORS["White"])
        self.preview = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT), pygame.SRCALPHA)

        # Состояния кисти
        self.tool = "pencil"
        self.color = COLORS["Black"]
        self.brush_size = 2
        
        self.drawing = False
        self.start_pos = (0, 0)
        self.last_pos = (0, 0)

        # Состояния для текста
        self.is_typing = False
        self.text_content = ""
        self.text_pos = (0, 0)
        self.font = pygame.font.SysFont(None, 36)

        # UI
        self.tools = ["pencil", "line", "eraser", "fill", "text", "rect", "square", "circle", "r_tri", "eq_tri", "rhomb"]
        self.tool_rects = {}
        self.color_rects = {}

    def draw_toolbar(self):
        pygame.draw.rect(self.screen, BG_COLOR, (0, 0, WIDTH, TOOLBAR_HEIGHT))
        pygame.draw.line(self.screen, COLORS["Black"], (0, TOOLBAR_HEIGHT-1), (WIDTH, TOOLBAR_HEIGHT-1), 2)

        font = pygame.font.SysFont(None, 20)
        
        # Отрисовка кнопок инструментов
        x, y = 10, 10
        for t in self.tools:
            color = (200, 200, 200) if self.tool == t else (255, 255, 255)
            rect = pygame.Rect(x, y, 70, 25)
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, COLORS["Black"], rect, 1)
            text = font.render(t, True, COLORS["Black"])
            self.screen.blit(text, (x + 5, y + 5))
            self.tool_rects[t] = rect
            x += 80
            if x > WIDTH - 100:
                x = 10
                y += 35

        # Отрисовка палитры цветов
        cx = WIDTH - 200
        for name, c_val in COLORS.items():
            rect = pygame.Rect(cx, 10, 25, 25)
            pygame.draw.rect(self.screen, c_val, rect)
            if self.color == c_val:
                pygame.draw.rect(self.screen, COLORS["Red"], rect, 3)
            else:
                pygame.draw.rect(self.screen, COLORS["Black"], rect, 1)
            self.color_rects[c_val] = rect
            cx += 30

        # Инфо
        info = font.render(f"Size (1,2,3): {self.brush_size}px", True, COLORS["Black"])
        self.screen.blit(info, (WIDTH - 200, 45))
        save_info = font.render("Ctrl+S to Save", True, COLORS["Black"])
        self.screen.blit(save_info, (WIDTH - 100, 45))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Сохранение (Ctrl+S)
                if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    filename = datetime.now().strftime("canvas_%Y%m%d_%H%M%S.png")
                    pygame.image.save(self.canvas, filename)
                    print(f"Saved as {filename}")
                
                # Горячие клавиши для размера кисти
                elif event.key == pygame.K_1: self.brush_size = 2
                elif event.key == pygame.K_2: self.brush_size = 5
                elif event.key == pygame.K_3: self.brush_size = 10

                # Обработка инструмента Текст
                if self.is_typing:
                    if event.key == pygame.K_RETURN:
                        text_surface = self.font.render(self.text_content, True, self.color)
                        self.canvas.blit(text_surface, self.text_pos)
                        self.is_typing = False
                        self.text_content = ""
                    elif event.key == pygame.K_ESCAPE:
                        self.is_typing = False
                        self.text_content = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.text_content = self.text_content[:-1]
                    else:
                        self.text_content += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if my < TOOLBAR_HEIGHT:
                    # Клик по тулбару
                    for t, rect in self.tool_rects.items():
                        if rect.collidepoint((mx, my)):
                            self.tool = t
                            self.is_typing = False
                    for c_val, rect in self.color_rects.items():
                        if rect.collidepoint((mx, my)):
                            self.color = c_val
                else:
                    # Клик по холсту
                    cx, cy = mx, my - TOOLBAR_HEIGHT
                    if self.tool == "fill":
                        target_color = self.canvas.get_at((cx, cy))
                        flood_fill(self.canvas, (cx, cy), target_color, self.color)
                    elif self.tool == "text":
                        self.is_typing = True
                        self.text_pos = (cx, cy)
                        self.text_content = ""
                    else:
                        self.drawing = True
                        self.start_pos = (cx, cy)
                        self.last_pos = (cx, cy)

            if event.type == pygame.MOUSEMOTION:
                if self.drawing:
                    cx, cy = event.pos[0], event.pos[1] - TOOLBAR_HEIGHT
                    if self.tool == "pencil":
                        pygame.draw.line(self.canvas, self.color, self.last_pos, (cx, cy), self.brush_size)
                        self.last_pos = (cx, cy)
                    elif self.tool == "eraser":
                        pygame.draw.line(self.canvas, COLORS["White"], self.last_pos, (cx, cy), self.brush_size * 5)
                        self.last_pos = (cx, cy)
                    else:
                        self.preview.fill((0, 0, 0, 0))
                        draw_shape(self.preview, self.tool, self.color, self.start_pos, (cx, cy), self.brush_size)

            if event.type == pygame.MOUSEBUTTONUP:
                if self.drawing:
                    cx, cy = event.pos[0], event.pos[1] - TOOLBAR_HEIGHT
                    if self.tool not in ["pencil", "eraser"]:
                        draw_shape(self.canvas, self.tool, self.color, self.start_pos, (cx, cy), self.brush_size)
                    self.drawing = False
                    self.preview.fill((0, 0, 0, 0))

    def run(self):
        while True:
            self.handle_events()
            
            # Отрисовка
            self.screen.fill(BG_COLOR)
            self.screen.blit(self.canvas, (0, TOOLBAR_HEIGHT))
            self.screen.blit(self.preview, (0, TOOLBAR_HEIGHT))
            self.draw_toolbar()

            # Предпросмотр текста
            if self.is_typing:
                text_surface = self.font.render(self.text_content + "|", True, self.color)
                self.screen.blit(text_surface, (self.text_pos[0], self.text_pos[1] + TOOLBAR_HEIGHT))

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    app = PaintApp()
    app.run()