import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = bool(re.match('[^A-Za-z0-9]', password))

    if length < 8:
        return "Weak"
    elif length < 12 and (not uppercase or not lowercase or not digit or not special_char):
        return "Medium"
    else:
        return "Strong"

def check_strength():
    password = password_entry.get()
    strength = check_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password Strength: {strength}")

def toggle_password_visibility():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_hide_button.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        show_hide_button.config(text="Show Password")

# Creating a GUI window
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("350x200")

# Creating label and entry for password
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Creating button to show/hide password
show_hide_button = tk.Button(root, text="Show Password", command=toggle_password_visibility)
show_hide_button.pack(pady=5)

# Creating button to check strength
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

#end of the code