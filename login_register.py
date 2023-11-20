import tkinter as tk
from tkinter import messagebox
import csv
import os
import re

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
            csvwriter.writerow(['Username', 'Password'])

    # Read existing users from the CSV file
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row
        users = [row for row in csvreader]

def register(file_path: str):
    global users

    username = username_entry.get()
    password = password_entry.get()

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
            "                     Error                     "
            "Password must have at least 1 uppercase letter,"
            "             1 special character,              "
            "       must be greater than 3 characters       "
            "          and less than 16 characters.         "
        )
    else:
        # Add the new user to the CSV file
        with open(file_path, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([username, password])
            messagebox.showinfo("Success", "Registration successful!")

        load_data(file_path)

# Function to log in an existing user
def login():
    """
    Log in an existing user.
    """

    global root, users
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password match
    if [username, password] in users:
        messagebox.showinfo("Success", "Login successful!")
        root.withdraw()  # Withdraw the login window
        root.destroy()   # Destroy the login window to close the program
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Variables
file_path = 'users.csv'
users = []

# Tkinter setup
root = tk.Tk()
root.title("Login/Register")

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