import tkinter as tk
from tkinter import messagebox
import sqlite3


def add_book_page(root):

    # Clear current window
    for widget in root.winfo_children():
        widget.destroy()

    # Heading
    tk.Label(
        root,
        text="Add New Book",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    # Book Title
    tk.Label(root, text="Book Title").pack()

    title_entry = tk.Entry(root, width=40)
    title_entry.pack(pady=5)

    # Author
    tk.Label(root, text="Author Name").pack()

    author_entry = tk.Entry(root, width=40)
    author_entry.pack(pady=5)

    # Quantity
    tk.Label(root, text="Quantity").pack()

    quantity_entry = tk.Entry(root, width=40)
    quantity_entry.pack(pady=5)

    def save_book():

        title = title_entry.get().strip()
        author = author_entry.get().strip()
        quantity = quantity_entry.get().strip()

        if title == "":
            messagebox.showerror("Error", "Enter Book Title")
            return

        if author == "":
            messagebox.showerror("Error", "Enter Author Name")
            return

        if quantity == "":
            messagebox.showerror("Error", "Enter Quantity")
            return

        try:
            quantity = int(quantity)

            if quantity < 0:
                messagebox.showerror(
                    "Error",
                    "Quantity cannot be negative"
                )
                return

        except ValueError:
            messagebox.showerror(
                "Error",
                "Quantity must be a number"
            )
            return

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO books(title, author, quantity)
            VALUES (?, ?, ?)
            """,
            (title, author, quantity)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Book Added Successfully"
        )

        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)

    def go_back():
        from pages.dashboard import open_dashboard
        open_dashboard(root)

    tk.Button(
        root,
        text="Save Book",
        width=20,
        bg="green",
        fg="white",
        command=save_book
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back",
        width=20,
        command=go_back
    ).pack(pady=5)