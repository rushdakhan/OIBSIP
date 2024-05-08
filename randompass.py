import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    try:
        length = int(password_length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Password length must be a number.")
        return
    
    if length < 4 or length > 32:
        messagebox.showerror("Error", "Password length must be between 4 and 32 characters.")
        return
    
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_result_label.config(text=password)


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("384x215")
root.config(background="darkseagreen1")

label = tk.Label(root, text="Random Password Generator",font=("Georgia",15,"bold"),pady=5,fg="red",bg="darkseagreen1")
label.grid(row=0,column=0,padx=40)

password_length_label = tk.Label(root, text="Enter Password Length:",font=("Georgia",15,"bold"),pady=5,fg="coral4",bg="darkseagreen1")
password_length_label.grid(row=1,column=0,padx=40)

password_length_entry = tk.Entry(root)
password_length_entry.grid(row=2,column=0,padx=5,pady=12)

generate_button = tk.Button(root, text="Generate Password", command=generate_password,bg="plum1", fg="purple4",font=("georgia", 13, "bold"),padx=2,pady=4)
generate_button.grid(row=3,column=0)

password_result_label = tk.Label(root, text="",bg="darkseagreen1",padx=5,pady=8,fg="red",font=("georgia",14, "bold"))
password_result_label.grid(row=4,column=0)

root.mainloop()