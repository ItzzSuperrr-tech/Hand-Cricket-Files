import pygame
import sys
from pygame.locals import * 
import tkinter
import animation

FPS=60

SCREENHEIGHT=1760
SCREENWIDTH=990

screen=pygame.display.set_mode((SCREENHEIGHT,SCREENWIDTH))

game_sprites={}
moving_sprites = pygame.sprite.Group()
playerx=int(SCREENWIDTH/5)
playery=int(SCREENHEIGHT/5)
player = animation.Player(playerx,playery)

moving_sprites.add(player)
game_sounds={}

#background and hand sign variables
background=('hand_cricket/gallery/sprites/background.png')
Title='hand_cricket/gallery/sprites/title.png'

def WelcomeScreen():


#Welcome Screen Title
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and event.key==(K_SPACE):
                return
            else:
                screen.blit(game_sprites['backgroundupdate'],(0,0))
                screen.blit(game_sprites['Titleupdate'],(0,10))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

if __name__=='__main__':
    pygame.init() #Initializes all pygame modules
    FPSCLOCK=pygame.time.Clock() #Control FPS for the game
    pygame.display.set_caption("Hand Cricket by Mahit Shah")

    game_sprites['Title']=pygame.image.load(Title).convert_alpha()
    Titleupdate=pygame.transform.scale(game_sprites['Title'],(SCREENHEIGHT,SCREENWIDTH))
    game_sprites['Titleupdate']=(Titleupdate)
    game_sounds['hand_beat']=pygame.mixer.Sound('hand_cricket/gallery/audio/hand_beat.wav')

    game_sprites['background']=pygame.image.load(background).convert()
    backgroundupdate=pygame.transform.scale(game_sprites['background'],(SCREENHEIGHT,SCREENWIDTH))
    game_sprites['backgroundupdate']=(backgroundupdate)

    while True:
        WelcomeScreen() #Shows the screen until any button is pressed
        animation.pygame.init()
        clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			player.attack()

	# Drawing
	screen.fill((0,0,0))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()


