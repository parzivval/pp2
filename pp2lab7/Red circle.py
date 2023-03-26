import pygame


pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Red circle")

ball_x = screen_width // 2
ball_y = screen_height // 2

ball_size = 50
ball_radius = 25

white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= 20
            elif event.key == pygame.K_DOWN:
                ball_y += 20
            elif event.key == pygame.K_LEFT:
                ball_x -= 20
            elif event.key == pygame.K_RIGHT:
                ball_x += 20

    if ball_x < ball_radius:
        ball_x = ball_radius
    elif ball_x > screen_width - ball_radius:
        ball_x = screen_width - ball_radius
    if ball_y < ball_radius:
        ball_y = ball_radius
    elif ball_y > screen_height - ball_radius:
        ball_y = screen_height - ball_radius

    screen.fill(white)

    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    clock.tick(60)