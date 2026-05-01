import pygame

def flood_fill(surface, pos, target_color, fill_color):
    """Алгоритм заливки (Flood-Fill) с использованием стека"""
    if target_color[:3] == fill_color[:3]:
        return
    
    stack = [pos]
    canvas_width, canvas_height = surface.get_size()

    while stack:
        x, y = stack.pop()
        # Проверяем совпадение цвета (игнорируя альфа-канал, если он есть)
        if surface.get_at((x, y))[:3] == target_color[:3]:
            surface.set_at((x, y), fill_color)
            if x > 0: stack.append((x - 1, y))
            if x < canvas_width - 1: stack.append((x + 1, y))
            if y > 0: stack.append((x, y - 1))
            if y < canvas_height - 1: stack.append((x, y + 1))

def draw_shape(surface, tool, color, start, end, size):
    """Логика отрисовки всех фигур"""
    x1, y1 = start
    x2, y2 = end
    
    if tool == "line":
        pygame.draw.line(surface, color, start, end, size)
    elif tool == "rect":
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(surface, color, rect, size)
    elif tool == "square":
        side = max(abs(x2 - x1), abs(y2 - y1))
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        rect = pygame.Rect(x1, y1, side * dx, side * dy)
        rect.normalize()
        pygame.draw.rect(surface, color, rect, size)
    elif tool == "circle":
        radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
        center = ((x1 + x2) // 2, (y1 + y2) // 2)
        if radius > size: 
            pygame.draw.circle(surface, color, center, radius, size)
    elif tool == "r_tri": 
        points = [(x1, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(surface, color, points, size)
    elif tool == "eq_tri": 
        mid_x = (x1 + x2) // 2
        points = [(mid_x, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(surface, color, points, size)
    elif tool == "rhomb": 
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
        pygame.draw.polygon(surface, color, points, size)