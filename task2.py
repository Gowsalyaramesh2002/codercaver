
import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    password_display.config(text=password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Label and Entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display generated password
password_display = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400)
password_display.pack()

root.mainloop()
