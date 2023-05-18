import tkinter as tk
from tkinter import messagebox
import subprocess

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Page")

        # Create a frame to hold the labels and entries
        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.RIGHT)

        # Set the font for the labels and entries
        font = ("Times New Roman", 16)

        # Add the logo image label
        #logo_image = tk.PhotoImage(file="logo.png")
        #self.logo_label = tk.Label(self.frame, image=logo_image)
        #self.logo_label.image = logo_image
        #self.logo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        self.welcome_label = tk.Label(self.frame, text="Welcome User..... Please login to continue", font=("Times New Roman", 24, "bold"), fg="red")
        self.welcome_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        self.username_label = tk.Label(self.frame, text="Username:", font=font)
        self.username_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.username_entry = tk.Entry(self.frame, font=font)
        self.username_entry.grid(row=2, column=1, padx=10, pady=10)

        self.password_label = tk.Label(self.frame, text="Password:", font=font)
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        self.password_entry = tk.Entry(self.frame, show="*", font=font)
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)

        self.show_password_var = tk.BooleanVar()
        self.show_password_var.set(False)
        self.show_password_checkbox = tk.Checkbutton(self.frame, text="Show Password", variable=self.show_password_var, font=font, command=self.toggle_password_visibility)
        self.show_password_checkbox.grid(row=4, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(row=5, column=1, padx=10, pady=10)

        # Create a label to hold the photo
        self.photo_label = tk.Label(self.master)
        self.photo_label.pack(side=tk.LEFT)

        # Load the photo from file and set it as the label's image
        photo = tk.PhotoImage(file="vsics_logo.png")
        self.photo_label.config(image=photo)
        self.photo_label.image = photo

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Replace this with your own authentication logic
        if username == "teacher" and password == "1234":
            messagebox.showinfo("Success", "Login successful!")
            self.master.destroy()
            subprocess.Popen(["python", "main.py"]) # Replace "main.py" with the name of your main file
        else:
            messagebox.showerror("Error", "Incorrect username or password")

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()