import pygame

def main():
    pygame.init()
    # Increased screen size slightly for more drawing space
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PyGame Extended Paint Program")
    clock = pygame.time.Clock()
    
    # Persistent surface to hold the drawn artwork
    canvas = pygame.Surface((800, 600))
    canvas.fill((0, 0, 0)) # black background
    
    radius = 15
    mode = 'draw'       # Available modes: 'draw', 'eraser', 'rect', 'circle'
    color = (0, 0, 255) # Start with Blue
    
    drawing = False
    start_pos = (0, 0)
    current_pos = (0, 0)
    last_pos = None

    # Font for our simple UI
    font = pygame.font.SysFont(None, 24)

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # --- Mode Selection ---
                if event.key == pygame.K_d:
                    mode = 'draw'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_r:
                    mode = 'rect'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                
                # --- Color Selection ---
                if event.key == pygame.K_1:
                    color = (255, 0, 0)     # Red
                elif event.key == pygame.K_2:
                    color = (0, 255, 0)     # Green
                elif event.key == pygame.K_3:
                    color = (0, 0, 255)     # Blue
                elif event.key == pygame.K_4:
                    color = (255, 255, 0)   # Yellow
                elif event.key == pygame.K_5:
                    color = (255, 255, 255) # White

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click to start drawing
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
                elif event.button == 4: # Scroll Up: Increase brush/line thickness
                    radius = min(200, radius + 2)
                elif event.button == 5: # Scroll Down: Decrease brush/line thickness
                    radius = max(1, radius - 2)
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    # Finalize rect or circle shape onto the main canvas when releasing left click
                    if mode == 'rect':
                        rect = pygame.Rect(start_pos[0], start_pos[1], current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])
                        rect.normalize()
                        pygame.draw.rect(canvas, color, rect, radius)
                    elif mode == 'circle':
                        dx = current_pos[0] - start_pos[0]
                        dy = current_pos[1] - start_pos[1]
                        dist = int((dx**2 + dy**2)**0.5)
                        # Pygame's circle crashes if width is greater than radius
                        draw_width = radius if radius < dist else 0
                        pygame.draw.circle(canvas, color, start_pos, dist, draw_width)

            elif event.type == pygame.MOUSEMOTION:
                current_pos = event.pos
                if drawing:
                    if mode == 'draw':
                        drawLineBetween(canvas, last_pos, current_pos, radius, color)
                    elif mode == 'eraser':
                        # Eraser paints over with the background color (Black)
                        drawLineBetween(canvas, last_pos, current_pos, radius, (0, 0, 0))
                    last_pos = current_pos

        # --- Rendering ---
        # 1. Blit the persistent canvas onto the screen
        screen.blit(canvas, (0, 0))
        
        # 2. Draw temporary live previews for shapes on the screen (not the canvas yet)
        if drawing:
            if mode == 'rect':
                rect = pygame.Rect(start_pos[0], start_pos[1], current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])
                rect.normalize()
                pygame.draw.rect(screen, color, rect, radius)
            elif mode == 'circle':
                dx = current_pos[0] - start_pos[0]
                dy = current_pos[1] - start_pos[1]
                dist = int((dx**2 + dy**2)**0.5)
                draw_width = radius if radius < dist else 0
                pygame.draw.circle(screen, color, start_pos, dist, draw_width)
        
        # 3. Draw On-Screen UI
        ui_text = f"Mode: {mode.capitalize()} (D/E/R/C) | Color: Keys 1-5 | Brush Size: {radius} (Scroll Wheel)"
        text_surface = font.render(ui_text, True, (200, 200, 200))
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(surface, start, end, width, color):
    """
    Adapted to apply a solid color between frames instead of using 
    an index-based color gradient, suiting a permanent drawing board.
    """
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    if iterations == 0:
        pygame.draw.circle(surface, color, start, width)
        return
        
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), width)

if __name__ == '__main__':
    main()