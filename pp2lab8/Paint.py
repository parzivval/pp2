import pygame

pygame.init()
running = True

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (500, 500)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(WINDOW_SIZE)

color = BLACK
shape = 'line'
clock = pygame.time.Clock()
pygame.display.set_caption('Paint')
screen.fill(WHITE)
width = 10
prev, cur = None, None

font = pygame.font.SysFont('Times New Roman', 15)


while running:
    pygame.draw.rect(screen, WHITE, (0, 0, WINDOW_WIDTH, 30))
    screen.blit(font.render(f'Function: {shape}', True, BLACK), (10, 400))
    screen.blit(font.render(f'Width: {width}', True, BLACK), (300, 400))
    screen.blit(font.render(f'Color: {color}', True, BLACK), (400, 400))
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_DOWN] and width > 1:
                width -= 1
            if pressed[pygame.K_UP]:
                width += 1
            if pressed[pygame.K_b]:
                color = BLUE
            if pressed[pygame.K_r]:
                color = RED
            if pressed[pygame.K_g]:
                color = GREEN
            if ctrl_pressed and pressed[pygame.K_c]:
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:
                shape = 'rectangle'
            if ctrl_pressed and pressed[pygame.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:
                shape = 'eraser'

        if shape == 'line' or shape == 'eraser':
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
                if prev:
                    if shape == 'line':
                        pygame.draw.line(screen, color, prev, cur, width)
                    if shape == 'eraser':
                        pygame.draw.line(screen, WHITE, prev, cur, width)
                    prev = cur
            if event.type == pygame.MOUSEBUTTONUP:
                prev = None
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                cur = pygame.mouse.get_pos()
                if shape == 'circle':
                    x = (prev[0]+cur[0])/2
                    y = (prev[1]+cur[1])/2
                    rx = abs(prev[0]-cur[0])/2
                    ry = abs(prev[1]-cur[1])/2
                    r = (rx + ry)/2
                    pygame.draw.circle(screen, color, (x, y), r, width)
                if shape == 'rectangle':
                    x = min(prev[0], cur[0])
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0]-cur[0])
                    ly = abs(prev[1]-cur[1])
                    pygame.draw.rect(screen, color, (x, y, lx, ly), width)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()