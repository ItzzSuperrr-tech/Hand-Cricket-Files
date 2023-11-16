import tkinter as tk
from tkinter import messagebox
import csv
import os

# Function to register a new user
def register():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username already exists
    if username in users:
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
    else:
        # Add the new user to the CSV file
        with open('users.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([username, password])
            messagebox.showinfo("Success", "Registration successful!")

# Function to log in an existing user
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password match
    if [username, password] in users:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Check if the CSV file exists, if not, create it
if not os.path.exists('users.csv'):
    with open('users.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Username', 'Password'])

# Read existing users from the CSV file
with open('users.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row
    users = [row for row in csvreader]

# Tkinter setup
root = tk.Tk()
root.title("Login/Register")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Username:").grid(row=0, column=0, pady=5)
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Password:").grid(row=1, column=0, pady=5)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, pady=5)

register_button = tk.Button(frame, text="Register", command=register)
register_button.grid(row=2, column=0, pady=10)

login_button = tk.Button(frame, text="Login", command=login)
login_button.grid(row=2, column=1, pady=10)

root.mainloop()
