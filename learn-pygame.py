import pygame
import sys

pygame.init()#Starts everything in pygame

screenheight = 1920
screenwidth = 1080
screen = pygame.display.set_mode((screenheight,screenwidth))
pygame.display.set_caption('Learner')
clock = pygame.time.Clock()

back_surface = pygame.Surface((screenheight,screenwidth))
back_surface.fill('grey')
player_surface = pygame.image.load(r'hand_cricket\gallery\sprites\player-removebg.png').convert_alpha()
computer_surface = pygame.image.load(r'hand_cricket\gallery\sprites\computer.png').convert_alpha()
classroom_surface = pygame.image.load(r"hand_cricket\gallery\sprites\classroom.png").convert_alpha()
bench_surface = pygame.image.load(r"hand_cricket\gallery\sprites\bench(2).png").convert_alpha()
#x_pos = -500


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(back_surface,(0,0))
    screen.blit(classroom_surface,(185,0))
    screen.blit(bench_surface,(720,684))
    screen.blit(player_surface,(185,684))
    pygame.display.update()
    clock.tick(100)