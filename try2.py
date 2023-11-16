import pygame
import sys
from tkinter import *

class Player(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
		animate.sprites = []
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(1).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(2).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(3).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(4).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(5).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(6).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(7).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(8).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(8).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(7).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(6).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(5).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(4).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(3).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(2).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(1).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(1).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(2).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(3).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(4).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(5).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(6).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(7).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(8).png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		animate.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		animate.current_sprite = 0
		animate.image = animate.sprites[animate.current_sprite]

		animate.rect = animate.image.get_rect()
		animate.rect.topleft = [pos_x,pos_y]

	def start(animate):
		animate.moving_animation = True

	def update(animate,speed):
		if animate.moving_animation == True:
			animate.current_sprite += speed
			if int(animate.current_sprite) >= len(animate.sprites):
				animate.current_sprite = 0
				animate.moving_animation = False

		animate.image = animate.sprites[int(animate.current_sprite)]
		
class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.flip_animation = False
        self.sprites = []  # Your coin sprite loading code...

        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-1.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-2.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-3.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-4.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-5.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-6.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-7.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-8.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-9.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-10.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-11.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-12.png'))
        self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\spirtes for coin flip animation\coin-13.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def flip(self):
        self.current_sprite = 0
        self.flip_animation = True

    def update(self, speed):
        if hasattr(self, 'flip_animation') and self.flip_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.flip_animation = False

            self.image = self.sprites[int(self.current_sprite)]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
player_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

coin = Coin(640,360)
player = Player(-500,-0)

player_sprites.add(player)
coin_sprites.add(coin)

back_surface = pygame.Surface((1280,720))
back_surface.fill('grey')

player_surface = pygame.image.load(r'hand_cricket\gallery\sprites\player-removebg.png').convert_alpha()
computer_surface = pygame.image.load(r'hand_cricket\gallery\sprites\computer.png').convert_alpha()
classroom_surface = pygame.image.load(r"hand_cricket\gallery\sprites\classroom(4,1080x720).png").convert_alpha()
bench_surface = pygame.image.load(r"hand_cricket\gallery\sprites\bench(2).png").convert_alpha()


# Tkinter code
def player_animation():
    player.start()
def coin_flip_animation():
    coin.flip()

window = Tk()
window.title('press buttons :)')
window.geometry("444x233")
window.minsize(300, 160)

#Frame
frame = Frame(window, padx=20, pady=20, bg='grey', borderwidth='15')
frame.pack(padx=10, pady=10,)

# Labels
label = Label(frame, text='Sprite Animation', font='comicsans 19 bold')
label.grid(row=0, column=0, columnspan=2, pady=10)

# Button for starting the animation in Pygame
player_button = Button(frame, text="1", command=player_animation)
player_button.grid(row=1, column=0, pady=5)

coin_button = Button(frame, text="Flip Coin Animation", command=coin_flip_animation)
coin_button.grid(row=2, column=0, pady=5)


# Your Pygame loop
def pygame_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(back_surface, (0, 0))
    screen.blit(classroom_surface, (100, 0))

    #draws and updates player's animation
    player_sprites.draw(screen)
    player_sprites.update(0.25)

    #draws and updates coins' animation
    coin_sprites.draw(screen)
    coin_sprites.update(0.25)

    clock.tick(30)
    pygame.display.flip()

    window.after(10, pygame_loop)  # Call the pygame_loop function after 10 milliseconds

pygame_loop()  # Start the pygame loop

window.mainloop()