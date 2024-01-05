import pygame
import sys
import tkinter as tk
import random

def maingame():

    # Animations
    class player(pygame.sprite.Sprite):
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
    Player_sprites = {}
    Player = {}

    print('Game Over')


    for i in range(1, 11):
        Player_sprites[i] = pygame.sprite.Group()
        Player[i] = player(-500, -0, i)
        Player_sprites[i].add(Player[i])

    Computer_sprites = {}
    Computer = {}

    for i in range(1, 11):
        Computer_sprites[i] = pygame.sprite.Group()
        Computer[i] = computer(-10, -0, i)
        Computer_sprites[i].add(Computer[i])

    back_surface = pygame.Surface((1280, 720))
    back_surface.fill('grey')

    title_font = pygame.font.Font(r'D:\New folder(to save)\code saves\hand_cricket\gallery\fonts_py\title_chalk.otf',90)
    text_font = pygame.font.Font(r'D:\New folder(to save)\code saves\hand_cricket\gallery\fonts_py\ARLRDBD.TTF',35)

    title_surface = title_font.render('Welcome to Hand Cricket', True, (100, 150, 200))
    Welcome_surface = text_font.render('User V/S Computer', True, (200, 00, 00))
    wdl_surface = text_font.render('W/D/L  :  W/D/L', True, (200, 100, 00))
    made_by_surface = text_font.render('Made by - Mahit Shah', True, (153, 153, 0))
    runs_surface = text_font.render('Runs: {runs_sum}', True, (00, 200, 200))

    classroom_surface = pygame.image.load(r"D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\blank_board_class.png").convert_alpha()  

    # tkinter code
    def random_num():
        random_num = random.randrange(1,11)
        return random_num
    
    def start_animation(i):
        global current1,current2,run_list,runs_sum
        Computer[random_num()].start()
        Player[i].start()
        current1 = i
        current2 = random_num
        return i

    window = tk.Tk()
    window.title('Press Buttons :)')
    window.geometry("400x250")
    window.minsize(400, 250)
    window.maxsize(400, 250)
    window.configure(bg='#F0F0F0')  # Set background color

    def play_inning(inning, current_runs, player_batting):
        # Variables for runs and innings

        if inning == 1:
            if player_batting is True:
                pass
            elif player_batting is False:
                pass
        elif inning == 2:
            if player_batting is True:
                pass
            elif player_batting is False:
                pass

    # Frame
    frame = tk.Frame(window, padx=20, pady=20, bg='#D0D0D0',borderwidth=5, relief=tk.GROOVE)
    frame.pack(padx=10, pady=10)

    # Labels
    label = tk.Label(frame, text='Choose Your Number',font=('Arial', 20, 'bold'), bg='#D0D0D0')
    label.grid(row=0, column=0, columnspan=5, pady=10)

    # Button for starting the animation in Pygame
    for row in range(2):
        for i in range(1, 6):
            player_button = tk.Button(frame,text=str(i + row*5),command=lambda i=i+row*5: start_animation(i),font=('Arial', 12),width=4,height=2)
            player_button.grid(row=row+1, column=i-1, pady=5)

    # Your Pygame loop
    def pygame_loop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(back_surface, (0, 0))
        screen.blit(classroom_surface, (100, 0))

        screen.blit(title_surface, (206,142))
        screen.blit(Welcome_surface, (356,242))
        screen.blit(wdl_surface, (656,242))
        screen.blit(runs_surface, (206,303))    
        screen.blit(made_by_surface, (656,303))

        # draws and updates player's animation
        try:
            Player_sprites[current1].draw(screen)
            Player_sprites[current1].update(0.25)
            Computer_sprites[current2].draw(screen)
            Computer_sprites[current2].update(0.25)
        except KeyError:
            Player_sprites[1].draw(screen)
            Player_sprites[1].update(0.25)
            Computer_sprites[1].draw(screen)
            Computer_sprites[1].update(0.25)
            pass

        clock.tick(120)
        pygame.display.flip()

        # Call the pygame_loop function after 10 milliseconds
        window.after(10, pygame_loop)

    current1 = None
    current2 = None
    pygame_loop()  # Start the pygame loop
    window.mainloop()

class CoinH(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.flip_animation = False
        self.sprites = []  # Coin sprite loading code...

        for i in range(4, 21):
            self.sprites.append(pygame.image.load(fr'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-'+str(i)+'.png'))

        for i in range(4, 5):
            self.sprites.append(pygame.image.load(
                r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-'+str(i)+'.png'
            ))

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

        for i in range(14, 21):
            self.sprites.append(pygame.image.load(fr'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-'+str(i)+'.png'))

        for i in range(1, 15):
            self.sprites.append(pygame.image.load(
                r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\ani2\coin-'+str(i)+'.png'
            ))

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

text_font = pygame.font.Font(r'D:\New folder(to save)\code saves\hand_cricket\gallery\fonts_py\PRISTINA.TTF',100)

win_text_surface = text_font.render('You won the toss :D', True, (255,215,0))
lose_text_surface = text_font.render('You lost :( Better Luck next time!', True, (255,215,0))
Continue_text_surface = text_font.render('PRESS ENTER TO CONTINUE', True, (255,215,0))
rect_win_surface = win_text_surface.get_rect(topleft = (310,0))
rect_lose_surface = lose_text_surface.get_rect( topleft = (100,0))
rect_con_surface = Continue_text_surface.get_rect(bottomleft = (5,720))

# tkinter code
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

window = tk.Tk()
window.title('press buttons :)')
window.minsize(350, 160)
window.maxsize(350, 160)

# Added this line to initialize the variable
window.x = None

#Frame
frame = tk.Frame(window, padx=4, pady=2, bg='grey', borderwidth='15')
frame.pack(padx=10, pady=10,)

# Labels
label = tk.Label(frame, text='Choose Heads or Tails', font='comicsans 19 bold')
label.grid(row=0, column=0, columnspan=2, pady=10)

# Button for starting the animation in Pygame
coin_button = tk.Button(frame, text="HEADS", command=Heads, relief='ridge', fg='white', bg='black', font='ink_free')
coin_button.grid(row=2, column=0, pady=5)

coin_button = tk.Button(frame, text="TAILS", command=Tails, relief='ridge', fg='white', bg='black', font='ink_free')
coin_button.grid(row=2, column=1, pady=5,)

# Second window
def display_tkinter_window():
    global window2
    window2 = tk.Tk()
    window2.title('Choose Bat or Bowl')
    window2.minsize(350, 160)
    window2.maxsize(350, 160)

    frame = tk.Frame(window2, padx=4, pady=2, bg='grey', borderwidth='15')
    frame.pack(padx=10, pady=10,)

    label = tk.Label(frame, text='Choose Bat or Bowl', font='comicsans 19 bold')
    label.grid(row=0, column=0, columnspan=2, pady=10)

    bat_button = tk.Button(frame, text="BAT", command=bat_selected, relief='ridge', fg='white', bg='black', font='ink_free')
    bat_button.grid(row=2, column=0, pady=5)

    bowl_button = tk.Button(frame, text="BOWL", command=bowl_selected, relief='ridge', fg='white', bg='black', font='ink_free')
    bowl_button.grid(row=2, column=1, pady=5)

    window2.mainloop()

def bat_selected():
    window2.x = 'batting'
    pygame.quit()
    window2.destroy()
    maingame()  
    sys.exit()

def bowl_selected():
    window2.x = 'bowling'
    pygame.quit()
    window2.destroy()
    maingame()
    sys.exit()

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
            window.destroy()
            display_tkinter_window()
            window.destroy()
        elif continuity == 0:
            window.destroy()
            maingame()
            window.destroy()
    clock.tick(120)
    pygame.display.flip()

    window.after(10, pygame_loop)  # Call the pygame_loop function after 10 milliseconds

pygame_loop()  # Start the pygame loop

window.mainloop()