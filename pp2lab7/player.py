import pygame
import os

pygame.init()
pygame.font.init()


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Music Player")
font = pygame.font.SysFont("arial", 15)

instruction_text = font.render("Press SPACE to play or stop the music, p to play previous song, and n to play next song", True, (0, 0, 0))

instruction_pos = (screen_width // 2 - instruction_text.get_width() // 2, screen_height - 50)


music_dir = "music"
music_files = [os.path.join(r'C:\Users\Бахытжан\Desktop\pp2\pp2lab7', f) for f in os.listdir(r'C:\Users\Бахытжан\Desktop\pp2\pp2lab7') if f.endswith(".mp3")]

pygame.mixer.init()
pygame.mixer.music.load(music_files[0])
current_music = 0
is_playing = False

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_playing = False
            elif event.key == pygame.K_n:
                current_music = (current_music + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music])
                pygame.mixer.music.play()
                is_playing = True
            elif event.key == pygame.K_p:
                current_music = (current_music - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music])
                pygame.mixer.music.play()
                is_playing = True


    screen.fill((255, 255, 255))


    screen.blit(instruction_text, instruction_pos)


    pygame.display.update()