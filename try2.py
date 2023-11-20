import pygame
import sys
import tkinter as Tk

#Sign 1 animation
class sign1(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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

	def start(animate):
		animate.moving_animation = True

	def update(animate,speed):
		if animate.moving_animation == True:
			animate.current_sprite += speed
			if int(animate.current_sprite) >= len(animate.sprites):
				animate.current_sprite = 0
				animate.moving_animation = False

		animate.image = animate.sprites[int(animate.current_sprite)]

#Sign 2 Animation
class sign2(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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

	def start(animate):
		animate.moving_animation = True

	def update(animate,speed):
		if animate.moving_animation == True:
			animate.current_sprite += speed
			if int(animate.current_sprite) >= len(animate.sprites):
				animate.current_sprite = 0
				animate.moving_animation = False

		animate.image = animate.sprites[int(animate.current_sprite)]

#Sign 3 Animation
class sign3(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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

	def start(animate):
		animate.moving_animation = True

	def update(animate,speed):
		if animate.moving_animation == True:
			animate.current_sprite += speed
			if int(animate.current_sprite) >= len(animate.sprites):
				animate.current_sprite = 0
				animate.moving_animation = False

		animate.image = animate.sprites[int(animate.current_sprite)]

#Sign 4 Animation
class sign4(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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

	def start(animate):
		animate.moving_animation = True

	def update(animate,speed):
		if animate.moving_animation == True:
			animate.current_sprite += speed
			if int(animate.current_sprite) >= len(animate.sprites):
				animate.current_sprite = 0
				animate.moving_animation = False

		animate.image = animate.sprites[int(animate.current_sprite)]

#Sign 5 Animation
class sign5(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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

	def start(animate):
		animate.moving_animation = True

	def update(animate,speed):
		if animate.moving_animation == True:
			animate.current_sprite += speed
			if int(animate.current_sprite) >= len(animate.sprites):
				animate.current_sprite = 0
				animate.moving_animation = False

		animate.image = animate.sprites[int(animate.current_sprite)]

#Sign 6 Animation
class sign6(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_6.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_6.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_6.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_6.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_1.png'))
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

#Sign 7 Animation
class sign7(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_7.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_7.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_7.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_7.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_7.png'))
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


#Sign 8 Animation
class sign8(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_8.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_8.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_8.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_8.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_8.png'))
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

#Sign 9 Animation
class sign9(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_9.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_9.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_9.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_9.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_9.png'))
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

#Sign 10 Animation
class sign10(pygame.sprite.Sprite):
	def __init__(animate, pos_x, pos_y):
		super().__init__()
		animate.moving_animation = False
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
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_10.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_10.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_10.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_10.png'))
		animate.sprites.append(pygame.image.load(r'gallery\sprites\hand_sign_10.png'))
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

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups

SN1_sprites = pygame.sprite.Group()
SN1 = sign1(-500,-0)
SN1_sprites.add(SN1)

SN2_sprites = pygame.sprite.Group()
SN2 = sign2(-500,-0)
SN2_sprites.add(SN2)

SN3_sprites = pygame.sprite.Group()
SN3 = sign3(-500,-0)
SN3_sprites.add(SN3)

SN4_sprites = pygame.sprite.Group()
SN4 = sign4(-500,-0)
SN4_sprites.add(SN4)

SN5_sprites = pygame.sprite.Group()
SN5 = sign5(-500,-0)
SN5_sprites.add(SN5)

SN6_sprites = pygame.sprite.Group()
SN6 = sign6(-500,-0)
SN6_sprites.add(SN6)

SN7_sprites = pygame.sprite.Group()
SN7 = sign7(-500,-0)
SN7_sprites.add(SN7)

SN8_sprites = pygame.sprite.Group()
SN8 = sign8(-500,-0)
SN8_sprites.add(SN8)

SN9_sprites = pygame.sprite.Group()
SN9 = sign9(-500,-0)
SN1_sprites.add(SN9)

SN10_sprites = pygame.sprite.Group()
SN10 = sign10(-500,-0)
SN10_sprites.add(SN10)

back_surface = pygame.Surface((1280,720))
back_surface.fill('grey')

classroom_surface = pygame.image.load(r"gallery\sprites\classroom(4,1080x720).png").convert_alpha()
bench_surface = pygame.image.load(r"gallery\sprites\bench(2).png").convert_alpha()

# Tkinter code
def SN1_animation():
    SN1.start()
    x = 1

def SN2_animation():
    SN2.start()
    x = 2

def SN3_animation():
    SN3.start()
    x = 3

def SN4_animation():
    SN4.start()
    x = 4

def SN5_animation():
    SN5.start()
    x = 5

def SN6_animation():
    SN6.start()
    x = 6

def SN7_animation():
    SN7.start()
    x = 7

def SN8_animation():
    SN8.start()
    x = 8

def SN9_animation():
    SN9.start()
    x = 9

def SN10_animation():
    SN10.start()
    x = 10

window = Tk.Tk()
window.title('Press Buttons :)')
window.geometry("400x250")
window.minsize(400,250)
window.maxsize(400,250)
window.configure(bg='#F0F0F0')  # Set background color

# Frame
frame = Tk.Frame(window, padx=20, pady=20, bg='#D0D0D0', borderwidth=5, relief=Tk.GROOVE)
frame.pack(padx=10, pady=10)

# Labels
label = Tk.Label(frame, text='Choose Your Number', font=('Arial', 20, 'bold'), bg='#D0D0D0')
label.grid(row=0, column=0, columnspan=5, pady=10)

# Button for starting the animation in Pygame
for i in range(1, 6):
    player_button = Tk.Button(frame, text=str(i), command=eval(f'SN{i}_animation'), font=('Arial', 12), width=4, height=2)
    player_button.grid(row=1, column=i-1, pady=5)
for i in range(1, 6):
    player_button = Tk.Button(frame, text=str(i+5), command=eval(f'SN{i+5}_animation'), font=('Arial', 12), width=4, height=2)
    player_button.grid(row=2, column=i-1, pady=5)

# Your Pygame loop
def pygame_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(back_surface, (0, 0))
    screen.blit(classroom_surface, (100, 0))

    #draws and updates player's animation

    SN1_sprites.draw(screen)
    SN1_sprites.update(0.25)

    SN2_sprites.draw(screen)
    SN2_sprites.update(0.25)

    SN3_sprites.draw(screen)
    SN3_sprites.update(0.25)

    SN4_sprites.draw(screen)
    SN4_sprites.update(0.25)

    SN5_sprites.draw(screen)
    SN5_sprites.update(0.25)

    SN6_sprites.draw(screen)
    SN6_sprites.update(0.25)

    SN7_sprites.draw(screen)
    SN7_sprites.update(0.25)

    SN8_sprites.draw(screen)
    SN8_sprites.update(0.25)

    SN9_sprites.draw(screen)
    SN9_sprites.update(0.25)

    SN10_sprites.draw(screen)
    SN10_sprites.update(0.25)

    clock.tick(120)
    pygame.display.flip()

    window.after(10, pygame_loop)  # Call the pygame_loop function after 10 milliseconds

pygame_loop()  # Start the pygame loop

window.mainloop()