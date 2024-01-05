import pygame
import sys
from tkinter import *

class Player(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.attack_animation = False
		animate.sprites = []
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(1).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(2).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(3).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(4).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(5).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(6).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(7).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(8).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(8).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(7).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(6).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(5).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(4).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(3).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(2).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(1).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(1).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(2).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(3).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(4).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(5).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(6).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(7).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\sprites for animation\player(8).png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_1.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_1.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_1.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_1.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_1.png'))
		animate.current_sprite = 0
		animate.image = animate.sprites[animate.current_sprite]

		animate.rect = animate.image.get_rect()
		animate.rect.topleft = [pos_x,pos_y]

	def attack(animate):
		animate.attack_animation = True

	def update(animate,speed):
		if animate.attack_animation == True:
			animate.current_sprite += speed
			if int(animate.current_sprite) >= len(animate.sprites):
				animate.current_sprite = 0
				animate.attack_animation = False

		animate.image = animate.sprites[int(animate.current_sprite)]

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
player_surface = pygame.image.load(r'gallery\sprites\player-removebg.png').convert_alpha()
computer_surface = pygame.image.load(r'gallery\sprites\computer.png').convert_alpha()
classroom_surface = pygame.image.load(r"gallery\sprites\classroom(4,1080x720).png").convert_alpha()
bench_surface = pygame.image.load(r"gallery\sprites\bench(2).png").convert_alpha()
back_surface.fill('grey')
#Button for animating
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.type == pygame.K_RETURN:
				pygame.quit()
				sys.exit()
		else:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					player.attack()

	# Drawing
	screen.blit(back_surface,(0,0))
	screen.blit(classroom_surface,(100,0))
   	# screen.blit(bench_surface,(480,456))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()
	
	clock.tick(120)