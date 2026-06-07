import tkinter as tk
from tkinter import messagebox
from pages.dashboard import open_dashboard


def login(root):

    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#f4f6f9")

    # Header
    header = tk.Frame(
        root,
        bg="#2C3E50",
        height=80
    )
    header.pack(fill="x")

    tk.Label(
        header,
        text="Library Management System",
        bg="#2C3E50",
        fg="white",
        font=("Arial", 22, "bold")
    ).pack(pady=20)

    # Main Container
    container = tk.Frame(
        root,
        bg="#f4f6f9"
    )
    container.pack(expand=True)

    # Login Card
    card = tk.Frame(
        container,
        bg="white",
        bd=2,
        relief="ridge",
        padx=30,
        pady=30
    )
    card.pack()

    tk.Label(
        card,
        text="Admin Login",
        bg="white",
        fg="#2C3E50",
        font=("Arial", 18, "bold")
    ).pack(pady=(0, 20))

    # Username
    tk.Label(
        card,
        text="Username",
        bg="white",
        font=("Arial", 11)
    ).pack(anchor="w")

    username = tk.Entry(
        card,
        width=35,
        font=("Arial", 11)
    )
    username.pack(pady=5)

    # Password
    tk.Label(
        card,
        text="Password",
        bg="white",
        font=("Arial", 11)
    ).pack(anchor="w")

    password = tk.Entry(
        card,
        width=35,
        show="*",
        font=("Arial", 11)
    )
    password.pack(pady=5)

    def check_login():

        user = username.get().strip()
        pwd = password.get().strip()

        if user == "admin" and pwd == "admin123":

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            open_dashboard(root)

        else:

            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )

    # Login Button
    tk.Button(
        card,
        text="Login",
        width=20,
        height=2,
        bg="#27AE60",
        fg="white",
        font=("Arial", 11, "bold"),
        command=check_login
    ).pack(pady=20)

    # Hint
    tk.Label(
        card,
        text="Default Login: admin / admin123",
        bg="white",
        fg="gray",
        font=("Arial", 9)
    ).pack()

    # Footer
    footer = tk.Label(
        root,
        text="Library Management System © 2026",
        bg="#2C3E50",
        fg="white",
        font=("Arial", 10)
    )
    footer.pack(side="bottom", fill="x")