import pygame
import tkinter
import time

#Display
width=1080
height=720
pygame.display.set_caption("Hand cricket")
gamewindow = pygame.display.set_mode((width, height))

background = pygame.image.load("gallery/sprites/bg-2.png")
backgroundupdate=pygame.transform.scale(background, (width,height))
hand=pygame.image.load('gallery/sprites/hand_sign_5.png')
handupdate = pygame.transform.scale(hand, (750,500))   
#Size of hand be (750,500)

def main():
    exit_game=False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            gamewindow.blit(backgroundupdate, (0,0))
            for i in range(10):

                gamewindow.blit(handupdate, (i,0))

            pygame.display.update()
    
if __name__=="__main__":
    main()