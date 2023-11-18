import pygame
import sys
import tkinter as Tk
import random

class CoinH(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.flip_animation = False
        self.sprites = []  # Your coin sprite loading code...

        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-4.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-5.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-6.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-7.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-8.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-9.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-10.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-11.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-12.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-13.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-14.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-15.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-16.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-17.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-18.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-19.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-20.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-1.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-2.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-3.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-4.png'))

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

class CoinT(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.flip_animation = False
        self.sprites = []  # Your coin sprite loading code...

        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-14.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-15.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-16.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-17.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-18.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-19.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-20.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-1.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-2.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-3.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-4.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-5.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-6.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-7.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-8.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-9.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-10.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-11.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-12.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-13.png'))
        self.sprites.append(pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-14.png'))

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

#Variables
cointoss=random.choice(['Heads','Tails'])
print()
print(cointoss)
print()
# Game Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
coin_sprites = pygame.sprite.Group()

if cointoss == 'Heads':
    coin = CoinH(490,210)
    coin_sprites.add(coin)
else:
    coin = CoinT(490,210)
    coin_sprites.add(coin)

back_surface = pygame.Surface((1280,720))
back_surface.fill('grey')

text_font = pygame.font.Font('hand_cricket\PRISTINA.TTF',100)

win_text_surface = text_font.render('You won the toss :D', True, (255,215,0))
lose_text_surface = text_font.render('You lost :( Better Luck next time!', True, (255,215,0))
Continue_text_surface = text_font.render('PRESS ENTER TO CONTINUE', True, (255,215,0))
rect_win_surface = win_text_surface.get_rect(topleft = (310,0))
rect_lose_surface = lose_text_surface.get_rect( topleft = (100,0))
rect_con_surface = Continue_text_surface.get_rect(bottomleft = (5,720))

# Tkinter code
def Heads():
    coin.flip()
    window.x = 'Heads'
    window.withdraw()
    pygame_loop()
    return True

def Tails():
    coin.flip()
    window.x = 'Tails'
    window.withdraw()
    pygame_loop()
    return True

window = Tk.Tk()
window.title('press buttons :)')
window.geometry("350x160")
window.minsize(350, 160)
window.maxsize(350, 160)

# Added this line to initialize the variable
window.x = None

#Frame
frame = Tk.Frame(window, padx=4, pady=2, bg='grey', borderwidth='15')
frame.pack(padx=10, pady=10,)

# Labels
label = Tk.Label(frame, text='Choose Heads or Tails', font='comicsans 19 bold')
label.grid(row=0, column=0, columnspan=2, pady=10)

# Button for starting the animation in Pygame
coin_button = Tk.Button(frame, text="HEADS", command=Heads, relief='ridge', fg='white', bg='black', font='ink_free')
coin_button.grid(row=2, column=0, pady=5)

coin_button = Tk.Button(frame, text="TAILS", command=Tails, relief='ridge', fg='white', bg='black', font='ink_free')
coin_button.grid(row=2, column=1, pady=5,)

# Second window
def display_tkinter_window():
    window = Tk.Tk()
    window.title('Choose Bat or Bowl')
    window.geometry("350x160")
    window.minsize(350, 160)
    window.maxsize(350, 160)

    frame = Tk.Frame(window, padx=4, pady=2, bg='grey', borderwidth='15')
    frame.pack(padx=10, pady=10,)

    label = Tk.Label(frame, text='Choose Bat or Bowl', font='comicsans 19 bold')
    label.grid(row=0, column=0, columnspan=2, pady=10)

    bat_button = Tk.Button(frame, text="BAT", command=bat_selected, relief='ridge', fg='white', bg='black', font='ink_free')
    bat_button.grid(row=2, column=0, pady=5)

    bowl_button = Tk.Button(frame, text="BOWL", command=bowl_selected, relief='ridge', fg='white', bg='black', font='ink_free')
    bowl_button.grid(row=2, column=1, pady=5)

    window.mainloop()

def bat_selected():
    print("You chose to BAT")
    # Add your logic for when the user chooses to BAT

def bowl_selected():
    print("You chose to BOWL")
    # Add your logic for when the user chooses to BOWL

# Your Pygame loop
def pygame_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(back_surface, (0, 0))
    coin_sprites.draw(screen)
    coin_sprites.update(0.25)

    # Check if a button is pressed
    if window.x is not None:
        # Check if the player's choice matches the coin toss result
        if window.x == cointoss:
            # Fill rect_win_surface with white
            pygame.draw.rect(screen, (0, 0, 0), rect_win_surface)
            pygame.draw.rect(screen, (0, 0, 0), rect_con_surface)
            screen.blit(win_text_surface, rect_win_surface)  # (310,0)
            screen.blit(Continue_text_surface, rect_con_surface)
            continuity=1
        else:
            # Fill rect_lose_surface with white
            pygame.draw.rect(screen, (0, 0, 0), rect_lose_surface)
            pygame.draw.rect(screen, (0, 0, 0), rect_con_surface)
            screen.blit(lose_text_surface, rect_lose_surface)  # (100,0)
            screen.blit(Continue_text_surface, rect_con_surface)
            continuity=0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        if continuity == 1:
            display_tkinter_window()
            window.destroy()
        elif continuity == 0:
            window.destroy()
    clock.tick(120)
    pygame.display.flip()

    window.after(10, pygame_loop)  # Call the pygame_loop function after 10 milliseconds

pygame_loop()  # Start the pygame loop

window.mainloop()