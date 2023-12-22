import tkinter as tk
from tkinter import messagebox
import csv
import os
import re
import pygame
import math
import sys

def load_data(file_path: str):
    """
    Load existing users from a CSV file.

    Args:
        file_path (str): The path to the CSV file.
    """

    global users

    # Check if the CSV file exists, if not, create it
    if not os.path.exists(file_path):
        with open('users.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Username', 'Password', 'W/D/L'])

    # Read existing users from the CSV file
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row
        users = [row for row in csvreader]

def register(file_path: str):
    global users, wdl 

    username = username_entry.get()
    password = password_entry.get()
    wdl = [0,0,0]

    # Check if username already exists
    if username in [user[0] for user in users]:
        messagebox.showerror(
            "Error",
            "Username already exists. Please choose a different username."
        )
    elif len(username) <= 3:
        messagebox.showerror(
            "Error",
            "Username must be more than 3 characters."
        )
    elif not re.search(r"[A-Z]", password):
        messagebox.showerror(
            "Error",
            "Password must have at least 1 uppercase letter, 1 special character and must be greater than 3 characters and less than 16 characters."
        )
    elif not re.search(r"[!@#$%^&_(){};:'/\|/?<>,.]",password):
        messagebox.showerror(
            "Error",
            "Password must have at least 1 uppercase letter, 1 special character and must be greater than 3 characters and less than 16 characters."
        )
    elif len(password) <=3 and len(password) > 16:
        messagebox.showerror(
            "Error",
            "Password must have at least 1 uppercase letter, 1 special character and must be greater than 3 characters and less than 16 characters."
        )
    elif not re.search(r"[013456789]",password):
        messagebox.showerror(
            "Error",
            "Password must have at least 1 uppercase letter, 1 special character and must be greater than 3 characters and less than 16 characters."
        )
    else:
        # Add the new user to the CSV file
        with open(file_path, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([username, password, wdl])
            messagebox.showinfo("Success", "Registration successful!")

        load_data(file_path)

# Function to log in an existing user
def login():
    """
    Log in an existing user.
    """

    global root, users, username
    username = username_entry.get()
    password = password_entry.get()
    users2 = []

    if len(users[0]) == 3:
        for i in users:
            i.pop(-1)
            users2.append(i)

    # Check if username and password match
    if [username, password] in users2:
            messagebox.showinfo("Success", "Login successful!")
            root.withdraw()  # Withdraw the login window
            root.destroy()   # Destroy the login window to close the program

    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Pygame Setup
pygame.init()
clock = pygame.time.Clock()

# Variables
file_path = 'users.csv'
users = []

# Tkinter setup
root = tk.Tk()
root.title("Login/Register")

root.minsize(350, 175)
root.maxsize(350, 175)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Increase font size for labels
tk.Label(frame, text="Username:", font=("Helvetica", 14)).grid(row=0, column=0, pady=5)
tk.Label(frame, text="Password:", font=("Helvetica", 14)).grid(row=1, column=0, pady=5)

# Increase font size for entry widgets
username_entry = tk.Entry(frame, font=("Helvetica", 12), width=20)
username_entry.grid(row=0, column=1, pady=5)

password_entry = tk.Entry(frame, show="*", font=("Helvetica", 12), width=20)
password_entry.grid(row=1, column=1, pady=5)

# Increase font size for buttons
register_button = tk.Button(
    frame,
    text="Register",
    command=lambda: register(file_path),
    font=("Helvetica", 12)
)
register_button.grid(row=2, column=0, pady=10)

login_button = tk.Button(
    frame,
    text="Login",
    command=login,
    font=("Helvetica", 12)
)
login_button.grid(row=2, column=1, pady=10)

load_data(file_path)
root.mainloop()

# Pygame Variables
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hand_Cricket")

title_font = pygame.font.Font(r'D:\New folder(to save)\code saves\hand_cricket\gallery\fonts_py\title_chalk.otf',90)
text_font = pygame.font.Font(r'D:\New folder(to save)\code saves\hand_cricket\gallery\fonts_py\ARLRDBD.TTF',35)

title_surface = title_font.render('Welcome to Hand Cricket', True, (100, 150, 200))
Welcome_surface = text_font.render(f'Welcome {username}', True, (200, 00, 00))
wdl_surface = text_font.render(f"W/D/L  :  ", True, (200, 100, 00))
enter_surface = text_font.render('Press Enter to continue', True, (00, 200, 200))
made_by_surface = text_font.render('Made by - Mahit Shah', True, (153, 153, 0))

back_surface = pygame.Surface((1280,720))
back_surface.fill('grey')

player_surface = pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\player-removebg.png').convert_alpha()
computer_surface = pygame.image.load(r'D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\computer_bg.png').convert_alpha()
classroom_surface = pygame.image.load(r"D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\blank_board_class.png").convert_alpha()
bench_surface = pygame.image.load(r"D:\New folder(to save)\code saves\hand_cricket\gallery\sprites\bench(2).png").convert_alpha()

y_pos = 389

center = [150,300]
r = 100

theta = 0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.quit()
                sys.exit()

    y = center[1] + r * math.sin(0.1 * theta)

    screen.blit(back_surface, (0, 0))
    screen.blit(classroom_surface, (100, 0))

    screen.blit(title_surface, (206,142))
    screen.blit(Welcome_surface, (306,242))
    screen.blit(wdl_surface, (656,242))
    screen.blit(enter_surface, (206,303))
    screen.blit(made_by_surface, (656,303))

    screen.blit(player_surface, (100, round(y) + 145))
    screen.blit(computer_surface, (725, round(y) + 145))
    theta += 0.1

    clock.tick(120)
    pygame.display.update()