import pygame
import math
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mickey's Clock")


mickey_image = pygame.image.load("mickey.jpg").convert_alpha()
mickey_rect = mickey_image.get_rect(center=(250, 250))


clock_radius = 200
clock_center = (250, 250)


minute_hand_length = 150
second_hand_length = 170


font = pygame.font.Font(None, 50)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, clock_center, clock_radius, 5)

    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = math.radians(90 - (minutes * 6))
    second_angle = math.radians(90 - (seconds * 6))

    minute_hand_image = pygame.transform.rotate(mickey_image, math.degrees(minute_angle))
    second_hand_image = pygame.transform.rotate(mickey_image, math.degrees(second_angle))

    minute_hand_rect = minute_hand_image.get_rect()
    minute_hand_rect.center = clock_center
    minute_hand_rect.move_ip(0, -minute_hand_length)
    screen.blit(minute_hand_image, minute_hand_rect)

    second_hand_rect = second_hand_image.get_rect()
    second_hand_rect.center = clock_center
    second_hand_rect.move_ip(0, -second_hand_length)
    screen.blit(second_hand_image, second_hand_rect)


    time_text = font.render("{:02d}:{:02d}".format(hours, minutes), True, BLACK)
    time_rect = time_text.get_rect(center=(250, 400))
    screen.blit(time_text, time_rect)


    pygame.display.flip()


    pygame.time.wait(1000 // 60)


pygame.quit()