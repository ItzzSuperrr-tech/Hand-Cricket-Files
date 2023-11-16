import random
import time
import sys
import pygame

from pygame.locals import *

#Game Variables
FPS=60

SCREENHEIGHT=1760
SCREENWIDTH=990

SCREEN=pygame.display.set_mode((SCREENHEIGHT,SCREENWIDTH))

game_sprites={}
game_sounds={}
#player variable
player=('hand_cricket/gallery/sprites/player.png')
computer=('hand_cricket/gallery/sprites/computer.png')

#background and hand sign variables
background=('hand_cricket/gallery/sprites/background.png')

Title='hand_cricket/gallery/sprites/title.png'

hand_sign1='hand_cricket/gallery/sprites/hand_sign_1.png'
hand_sign2='hand_cricket/gallery/sprites/hand_sign_2.png'
hand_sign3='hand_cricket/gallery/sprites/hand_sign_3.png'
hand_sign4='hand_cricket/gallery/sprites/hand_sign_4.png'
hand_sign5='hand_cricket/gallery/sprites/hand_sign_5.png'
hand_sign6='hand_cricket/gallery/sprites/hand_sign_6.png'
hand_sign7='hand_cricket/gallery/sprites/hand_sign_7.png'
hand_sign8='hand_cricket/gallery/sprites/hand_sign_8.png'
hand_sign9='hand_cricket/gallery/sprites/hand_sign_9.png'
hand_sign10='hand_cricket/gallery/sprites/hand_sign_10.png'

#game variables
battingscorebyplayer=0
bowlingscorebycomputer=0

player_throws_batting=0
computer_random_batting=0

player_throws_bowling=1
computer_random_bowling=1

#WELCOME SCREEN FUNCTION

def WelcomeScreen():
#player
    playerx=int(SCREENWIDTH/5)
    playery=int(SCREENHEIGHT-game_sprites['player'].get_height())
#computer
    computerx=int(SCREENWIDTH/10)
    computery=int(SCREENHEIGHT-game_sprites['player'].get_height())

#Welcome Screen Title
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and event.key==(K_SPACE):
                return
            else:
                SCREEN.blit(game_sprites['backgroundupdate'],(0,0))
                SCREEN.blit(game_sprites['playerupdate'],(-720,100))
                SCREEN.blit(game_sprites['computerupdate'],(100,100))
                SCREEN.blit(game_sprites['Titleupdate'],(0,10))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def maingame():
    pass


if __name__=='__main__':
    pygame.init() #Initializes all pygame modules
    FPSCLOCK=pygame.time.Clock() #Control FPS for the game
    pygame.display.set_caption("Hand Cricket by Mahit Shah")
    game_sprites['hand_signs']=(
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_1.png').convert_alpha(),
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_2.png').convert_alpha(),
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_3.png').convert_alpha(),
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_4.png').convert_alpha(),
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_5.png').convert_alpha(),
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_6.png').convert_alpha(),
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_7.png').convert_alpha(),
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_8.png').convert_alpha(),
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_9.png').convert_alpha(),
        pygame.image.load('hand_cricket/gallery/sprites/hand_sign_10.png').convert_alpha()
    )

    game_sprites['player']=pygame.image.load(player).convert_alpha()
    playerupdate=pygame.transform.scale(game_sprites['player'],(1920,1080))
    game_sprites['playerupdate']=(playerupdate)
    game_sprites['computer']=pygame.image.load(computer).convert_alpha()
    computerupdate=pygame.transform.scale(game_sprites['computer'],(1920,1080))
    game_sprites['computerupdate']=(computerupdate)

    game_sprites['Title']=pygame.image.load(Title).convert_alpha()
    Titleupdate=pygame.transform.scale(game_sprites['Title'],(SCREENHEIGHT,SCREENWIDTH))
    game_sprites['Titleupdate']=(Titleupdate)
    game_sounds['hand_beat']=pygame.mixer.Sound('hand_cricket/gallery/audio/hand_beat.wav')

    game_sprites['background']=pygame.image.load(background).convert()
    backgroundupdate=pygame.transform.scale(game_sprites['background'],(SCREENHEIGHT,SCREENWIDTH))
    game_sprites['backgroundupdate']=(backgroundupdate)

    while True:
        WelcomeScreen() #Shows the screen until any button is pressed
        maingame() #Starts the main game