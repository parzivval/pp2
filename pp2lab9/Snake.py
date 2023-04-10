import time
import random
import pygame

snake_speed = 15
start_time = time.time()
window_x = 720
window_y = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pygame.init()
pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()
snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

direction = 'RIGHT'
change_to = direction

score = 0
level = 1
# added timer variables
fruit_timer = 5000 # time in milliseconds
start_time = pygame.time.get_ticks()
current_time = start_time
def generate_fruit():
    fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    fruit_points = random.randrange(1, 4) * 10
    return fruit_position, fruit_points

fruit_position, fruit_points = generate_fruit()
fruit_spawn = True
fruit_respawn_delay = 500  # milliseconds
last_fruit_spawn_time = pygame.time.get_ticks()

def draw_fruit():
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score) + '  Speed: ' + str(snake_speed), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (window_x // 5, 10)
    else:
        score_rect.midtop = (window_x // 2, window_y // 1.25)
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your score is : ' + str(score), True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(2, white, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    # added timer check
    current_time = pygame.time.get_ticks()
    if current_time - start_time > fruit_timer:
        fruit_spawn = False
        start_time = current_time
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += fruit_points
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position, fruit_points = generate_fruit()
        fruit_spawn = True
        last_fruit_spawn_time = pygame.time.get_ticks()

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    draw_fruit()
    show_score(1, white, 'consolas', 20)

    if (snake_position[0] < 0 or snake_position[0] > window_x-10 or
            snake_position[1] < 0 or snake_position[1] > window_y-10):
        game_over()

    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    if score >= 50 and score < 100:
        snake_speed = 20
        level = 2
    elif score >= 100 and score < 150:
        snake_speed = 25
        level = 3
    elif score >= 150:
        snake_speed = 30
        level = 4

    fps.tick(snake_speed)

    pygame.display.update()