import pygame
import sys
from tkinter import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(1).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(2).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(3).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(4).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(5).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(6).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(7).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(8).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(8).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(7).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(6).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(5).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(4).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(3).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(2).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(1).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(1).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(2).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(3).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(4).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(5).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(6).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(7).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\sprites for animation\player(8).png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		self.sprites.append(pygame.image.load('hand_cricket\gallery\sprites\hand_sign_1.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(-500,0)
moving_sprites.add(player)
back_surface = pygame.Surface((1280,720))
player_surface = pygame.image.load(r'hand_cricket\gallery\sprites\player-removebg.png').convert_alpha()
computer_surface = pygame.image.load(r'hand_cricket\gallery\sprites\computer.png').convert_alpha()
classroom_surface = pygame.image.load(r"hand_cricket\gallery\sprites\classroom(4,1080x720).png").convert_alpha()
bench_surface = pygame.image.load(r"hand_cricket\gallery\sprites\bench(2).png").convert_alpha()
back_surface.fill('grey')
#Button for animating
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.quit()
		else:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					player.attack()


	# Drawing
	screen.blit(back_surface,(0,0))
	screen.blit(classroom_surface,(100,0))
#	screen.blit(bench_surface,(480,456))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()
	
	clock.tick(120)
	
