import pygame
import sys
import tkinter as Tk
import random as r

# Animations
class computer(pygame.sprite.Sprite):
    def __init__(animate, pos_x, pos_y, number):
        super().__init__()
        animate.moving_animation = False
        animate.sprites = []
        animate.number = number

        for i in range(1, 9):
            animate.sprites.append(pygame.image.load(
                fr'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\sprites for animation\player('+str(i)+').png'
            ))
        for i in range(8, 0, -1):
            animate.sprites.append(pygame.image.load(
                fr'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\sprites for animation\player('+str(i)+').png'
            ))
        for i in range(1, 9):
            animate.sprites.append(pygame.image.load(
                fr'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\sprites for animation\player('+str(i)+').png'
            ))

        animate.sprites.append(pygame.image.load(
            fr'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\hand_sign_{animate.number}.png'
        ))

        animate.current_sprite = 0
        animate.image = animate.sprites[animate.current_sprite]

        animate.rect = animate.image.get_rect()
        animate.rect.topleft = [pos_x, pos_y]

    def start(animate):
        animate.current_sprite = 0
        animate.moving_animation = True

    def update(animate, speed):
        if animate.moving_animation:
            animate.current_sprite += speed
            if int(animate.current_sprite) >= len(animate.sprites):
                animate.current_sprite = len(animate.sprites) - 1
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
Computer_sprites = {}
Computer = {}

for i in range(1, 11):
    Computer_sprites[i] = pygame.sprite.Group()
    Computer[i] = computer(-10, -0, i)
    Computer_sprites[i].add(Computer[i])

back_surface = pygame.Surface((1280, 720))
back_surface.fill('grey')

classroom_surface = pygame.image.load(
    r"D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\classroom(4,1080x720).png"
).convert_alpha()
bench_surface = pygame.image.load(
    r"D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\bench(2).png"
).convert_alpha()


# Tkinter code
def start_animation():
    global current
    random_num = r.randrange(1,11)
    Computer[random_num].start()
    current = random_num


window = Tk.Tk()
window.title('Press Buttons :)')
window.geometry("400x250")
window.minsize(400, 250)
window.maxsize(400, 250)
window.configure(bg='#F0F0F0')  # Set background color

# Frame
frame = Tk.Frame(window, padx=20, pady=20, bg='#D0D0D0',
                 borderwidth=5, relief=Tk.GROOVE)
frame.pack(padx=10, pady=10)

# Labels
label = Tk.Label(frame, text='Choose Your Number',
                 font=('Arial', 20, 'bold'), bg='#D0D0D0')
label.grid(row=0, column=0, columnspan=5, pady=10)

# Button for starting the animation in Pygame
player_button = Tk.Button(frame,text='click',command=lambda : start_animation(),font=('Arial', 12),width=4,height=2)
player_button.grid(row=4, column=1, pady=5)

# Your Pygame loop
def pygame_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(back_surface, (0, 0))
    screen.blit(classroom_surface, (100, 0))

    # draws and updates player's animation
    try:
        Computer_sprites[current].draw(screen)
        Computer_sprites[current].update(0.25)
    except KeyError:
        Computer_sprites[1].draw(screen)
        Computer_sprites[1].update(0.25)
        pass

    clock.tick(120)
    pygame.display.flip()

    # Call the pygame_loop function after 10 milliseconds
    window.after(10, pygame_loop)


current = None
pygame_loop()  # Start the pygame loop
window.mainloop()
