import random
import string
import tkinter as tk
from tkinter import messagebox
def generate_password():
    length = int(length_entry.get())
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_special_chars = special_chars_var.get()
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if not characters:
        messagebox.showerror("Error", "Please select at least one character set.")
        return
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated Password: " + password)
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#f2f2f2")
length_label = tk.Label(root, text="Password Length:", bg="#f2f2f2")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)
lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(root, text="Lowercase Letters", variable=lowercase_var, bg="#f2f2f2")
lowercase_check.grid(row=1, column=0, padx=10, pady=5, sticky="w")
uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var, bg="#f2f2f2")
uppercase_check.grid(row=2, column=0, padx=10, pady=5, sticky="w")
numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Numbers", variable=numbers_var, bg="#f2f2f2")
numbers_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")
special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var, bg="#f2f2f2")
special_chars_check.grid(row=4, column=0, padx=10, pady=5, sticky="w")
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#007acc", fg="white")
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
result_label = tk.Label(root, text="", bg="#f2f2f2", font=("Helvetica", 12))
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
for i in range(7):  
    root.grid_rowconfigure(i, pad=5)
root.grid_columnconfigure(1, pad=5)
root.mainloop()
