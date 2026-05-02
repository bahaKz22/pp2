import pygame

def draw_shape(surface, tool, color, x1, y1, x2, y2, thick):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    if width == 0 or height == 0:
        return

    if tool == "rect":
        pygame.draw.rect(surface, color, (min(x1, x2), min(y1, y2), width, height), thick)
    elif tool == "square":
        side = max(width, height)
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        sq_x = min(x1, x1 + side * dx)
        sq_y = min(y1, y1 + side * dy)
        pygame.draw.rect(surface, color, (sq_x, sq_y, side, side), thick)
    elif tool == "r_tri":
        pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)], thick)
    elif tool == "eq_tri":
        mx = (x1 + x2) / 2
        pygame.draw.polygon(surface, color, [(mx, y1), (x1, y2), (x2, y2)], thick)
    elif tool == "rhomb":
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        pygame.draw.polygon(surface, color, [(mx, y1), (x2, my), (mx, y2), (x1, my)], thick)

# Инициализация
pygame.init()
pygame.font.init()

# Чуть расширили окно, чтобы влезли новые кнопки
W, H = 900, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Мой Paint на Pygame")

canvas = pygame.Surface((W, H))
canvas.fill((255, 255, 255))
font = pygame.font.SysFont("Arial", 15)

# Кнопки инструментов и толщины
buttons = [
    ("Карандаш", "pencil", pygame.Rect(10, 10, 75, 30)),
    ("Ластик", "eraser", pygame.Rect(90, 10, 60, 30)),
    ("Прямоуг.", "rect", pygame.Rect(155, 10, 75, 30)),
    ("Квадрат", "square", pygame.Rect(235, 10, 65, 30)),
    ("Пр. треуг", "r_tri", pygame.Rect(305, 10, 75, 30)),
    ("Равн. треуг", "eq_tri", pygame.Rect(385, 10, 85, 30)),
    ("Ромб", "rhomb", pygame.Rect(475, 10, 50, 30)),
    ("-", "minus", pygame.Rect(535, 10, 20, 30)),  # Кнопка уменьшения толщины
    ("+", "plus", pygame.Rect(560, 10, 20, 30))   # Кнопка увеличения толщины
]

# Палитра цветов (список RGB)
colors = [
    (0, 0, 0),       # Черный
    (255, 0, 0),     # Красный
    (0, 255, 0),     # Зеленый
    (0, 0, 255),     # Синий
    (255, 255, 0),   # Желтый
    (255, 165, 0),   # Оранжевый
    (128, 0, 128)    # Фиолетовый
]

# Размещаем палитру правее
color_rects = []
start_c_x = 700
for i in range(len(colors)):
    color_rects.append(pygame.Rect(start_c_x + i * 25, 12, 20, 20))

# Начальные настройки
current_tool = "pencil"
current_color = (0, 0, 0)
thickness = 2 # Начальная толщина
drawing = False
start_x, start_y = 0, 0
last_x, last_y = 0, 0

running = True
while running:
    # 1. ОТРИСОВКА
    screen.blit(canvas, (0, 0))
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if drawing and current_tool not in ["pencil", "eraser"] and mouse_y > 50:
        draw_shape(screen, current_tool, current_color, start_x, start_y, mouse_x, mouse_y, thickness)
        
    pygame.draw.rect(screen, (220, 220, 220), (0, 0, W, 50))
    pygame.draw.line(screen, (150, 150, 150), (0, 50), (W, 50), 2)
    
    # Рисуем кнопки инструментов
    for text, tool, rect in buttons:
        bg_color = (150, 150, 150) if tool == current_tool else (200, 200, 200)
        pygame.draw.rect(screen, bg_color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 1)
        
        # Центрируем текст на кнопках + и -
        if tool in ["plus", "minus"]:
            txt_surface = font.render(text, True, (0, 0, 0))
            screen.blit(txt_surface, (rect.x + 6, rect.y + 5))
        else:
            txt_surface = font.render(text, True, (0, 0, 0))
            screen.blit(txt_surface, (rect.x + 5, rect.y + 5))

    # Выводим текущую толщину текстом
    thick_text = font.render(f"Толщина: {thickness}", True, (0, 0, 0))
    screen.blit(thick_text, (590, 15))

    # Рисуем палитру цветов
    for i, rect in enumerate(color_rects):
        pygame.draw.rect(screen, colors[i], rect)
        border = 3 if colors[i] == current_color else 1
        pygame.draw.rect(screen, (0, 0, 0), rect, border)

    pygame.display.flip()

    # 2. СОБЫТИЯ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Управление толщиной через колесико мыши
        elif event.type == pygame.MOUSEWHEEL:
            thickness += event.y # event.y равен 1 (крутим вверх) или -1 (крутим вниз)
            if thickness < 1:
                thickness = 1
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked_ui = False
                
                # Проверка клика по инструментам
                for text, tool, rect in buttons:
                    if rect.collidepoint(event.pos):
                        clicked_ui = True
                        if tool == "plus":
                            thickness += 1
                        elif tool == "minus":
                            thickness = max(1, thickness - 1)
                        else:
                            current_tool = tool
                        break
                
                # Проверка клика по палитре цветов
                if not clicked_ui:
                    for i, rect in enumerate(color_rects):
                        if rect.collidepoint(event.pos):
                            current_color = colors[i]
                            clicked_ui = True
                            break
                        
                # Начало рисования
                if not clicked_ui and event.pos[1] > 50:
                    drawing = True
                    start_x, start_y = event.pos
                    last_x, last_y = event.pos
                    
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_tool == "pencil":
                    pygame.draw.line(canvas, current_color, (last_x, last_y), event.pos, thickness)
                elif current_tool == "eraser":
                    # Ластик делаем в 3 раза толще кисти, чтобы было удобнее стирать
                    pygame.draw.line(canvas, (255, 255, 255), (last_x, last_y), event.pos, thickness * 3)
                last_x, last_y = event.pos
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                if current_tool not in ["pencil", "eraser"]:
                    draw_shape(canvas, current_tool, current_color, start_x, start_y, event.pos[0], event.pos[1], thickness)
                    
pygame.quit()