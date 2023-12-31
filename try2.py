import pygame
import sys
import tkinter as Tk


# Sign 1 animation
class signs(pygame.sprite.Sprite):
    def __init__(animate, pos_x, pos_y, number):
        super().__init__()
        animate.moving_animation = False
        animate.sprites = []
        animate.number = number

        for i in range(1, 9):
            animate.sprites.append(pygame.image.load(
                r"'gallery\sprites\sprites for animation\player('+str(i)+').png'"
            ))
        for i in range(8, 0, -1):
            animate.sprites.append(pygame.image.load(
                r"'gallery\sprites\sprites for animation\player('+str(i)+').png'"
            ))
        for i in range(1, 9):
            animate.sprites.append(pygame.image.load(
                r"'gallery\sprites\sprites for animation\player('+str(i)+').png'"
            ))

        for i in range(3):
            animate.sprites.append(pygame.image.load(
                fr'gallery\sprites\hand_sign_{animate.number}.png'
            ))

        animate.current_sprite = 0
        animate.image = animate.sprites[animate.current_sprite]

        animate.rect = animate.image.get_rect()
        animate.rect.topleft = [pos_x, pos_y]

    def start(animate):
        animate.moving_animation = True

    def update(animate, speed):
        if animate.moving_animation:
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
SN_sprites = {}
SN = {}

for i in range(1, 11):
    SN_sprites[i] = pygame.sprite.Group()
    SN[i] = signs(-500, -0, i)
    SN_sprites[i].add(SN[i])

back_surface = pygame.Surface((1280, 720))
back_surface.fill('grey')

classroom_surface = pygame.image.load(
    r"gallery\sprites\classroom(4,1080x720).png"
).convert_alpha()
bench_surface = pygame.image.load(
    r"gallery\sprites\bench(2).png"
).convert_alpha()


# Tkinter code
def start_animation(i):
    SN[i].start()


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
for i in range(1, 6):
    player_button = Tk.Button(
        frame,
        text=str(i),
        command=lambda i=i: start_animation(i),
        font=('Arial', 12),
        width=4,
        height=2
    )
    player_button.grid(row=1, column=i-1, pady=5)

for i in range(1, 6):
    player_button = Tk.Button(
        frame, text=str(i+5),
        command=lambda i=i: start_animation(i+5),
        font=('Arial', 12),
        width=4,
        height=2
    )
    player_button.grid(row=2, column=i-1, pady=5)


# Your Pygame loop
def pygame_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(back_surface, (0, 0))
    screen.blit(classroom_surface, (100, 0))

    # draws and updates player's animation
    for i in range(1, 11):
        SN_sprites[i].draw(screen)
        SN_sprites[i].update(0.25)

    clock.tick(120)
    pygame.display.flip()

    # Call the pygame_loop function after 10 milliseconds
    window.after(10, pygame_loop)


pygame_loop()  # Start the pygame loop

window.mainloop()
