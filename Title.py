import pygame
import sys
import math

#General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hand_Cricket")

title_font = pygame.font.Font(r'D:\New folder(to save)\code saves\hand_cricket\gallery\fonts_py\title_chalk.otf',90)
text_font = pygame.font.Font(r'D:\New folder(to save)\code saves\hand_cricket\gallery\fonts_py\ARLRDBD.TTF',35)

title_surface = title_font.render('Welcome to Hand Cricket', True, (100, 150, 200))
Welcome_surface = text_font.render('Welcome User', True, (200, 00, 00))
wdl_surface = text_font.render('W/D/L  :  W/D/L', True, (200, 100, 00))
enter_surface = text_font.render('Press Enter to continue', True, (00, 200, 200))
made_by_surface = text_font.render('Made by - Mahit Shah', True, (153, 153, 0))

back_surface = pygame.Surface((1280,720))
back_surface.fill('grey')

player_surface = pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\player-removebg.png').convert_alpha()
computer_surface = pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\computer_bg.png').convert_alpha()
classroom_surface = pygame.image.load(r"D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\blank_board_class.png").convert_alpha()
bench_surface = pygame.image.load(r"D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\bench(2).png").convert_alpha()

y_pos = 389

center = [150,300]
r = 100

theta = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.quit()
                sys.exit()

    y = center[1] + r * math.sin(0.1 * theta)

    screen.blit(back_surface, (0, 0))
    screen.blit(classroom_surface, (100, 0))

    screen.blit(title_surface, (206,142))
    screen.blit(Welcome_surface, (356,242))
    screen.blit(wdl_surface, (656,242))
    screen.blit(enter_surface, (206,303))
    screen.blit(made_by_surface, (656,303))

    screen.blit(player_surface, (100, round(y) + 145))
    screen.blit(computer_surface, (725, round(y) + 145))
    theta += 0.1

    clock.tick(120)
    pygame.display.update()
