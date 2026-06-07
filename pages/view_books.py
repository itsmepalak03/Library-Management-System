import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def view_books_page(root):

    # Clear window
    for widget in root.winfo_children():
        widget.destroy()

    # Title
    tk.Label(
        root,
        text="View Books",
        font=("Arial", 20, "bold")
    ).pack(pady=10)

    # Search Section
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    tk.Label(
        search_frame,
        text="Search Book:"
    ).pack(side="left")

    search_entry = tk.Entry(
        search_frame,
        width=30
    )
    search_entry.pack(side="left", padx=5)

    # Edit Fields
    tk.Label(root, text="Book Title").pack()

    title_entry = tk.Entry(root, width=40)
    title_entry.pack(pady=2)

    tk.Label(root, text="Author").pack()

    author_entry = tk.Entry(root, width=40)
    author_entry.pack(pady=2)

    tk.Label(root, text="Quantity").pack()

    quantity_entry = tk.Entry(root, width=40)
    quantity_entry.pack(pady=2)

    # Table
    columns = (
        "ID",
        "Title",
        "Author",
        "Quantity"
    )

    tree = ttk.Treeview(
        root,
        columns=columns,
        show="headings",
        height=12
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(pady=10)

    # Load Books
    def load_books():

        tree.delete(*tree.get_children())

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM books"
        )

        rows = cursor.fetchall()

        conn.close()

        for row in rows:
            tree.insert(
                "",
                tk.END,
                values=row
            )

    # Search Book
    def search_book():

        keyword = search_entry.get().strip()

        tree.delete(*tree.get_children())

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM books
            WHERE title LIKE ?
            """,
            ('%' + keyword + '%',)
        )

        rows = cursor.fetchall()

        conn.close()

        for row in rows:
            tree.insert(
                "",
                tk.END,
                values=row
            )

    # Select Book
    def select_book(event):

        selected = tree.focus()

        values = tree.item(
            selected,
            "values"
        )

        if values:

            title_entry.delete(0, tk.END)
            author_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)

            title_entry.insert(
                0,
                values[1]
            )

            author_entry.insert(
                0,
                values[2]
            )

            quantity_entry.insert(
                0,
                values[3]
            )

    tree.bind(
        "<ButtonRelease-1>",
        select_book
    )

    # Update Book
    def update_book():

        selected = tree.focus()

        values = tree.item(
            selected,
            "values"
        )

        if not values:
            messagebox.showerror(
                "Error",
                "Select a book first"
            )
            return

        book_id = values[0]

        title = title_entry.get().strip()
        author = author_entry.get().strip()
        quantity = quantity_entry.get().strip()

        if title == "" or author == "" or quantity == "":
            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return

        try:
            quantity = int(quantity)
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
            UPDATE books
            SET title=?,
                author=?,
                quantity=?
            WHERE id=?
            """,
            (
                title,
                author,
                quantity,
                book_id
            )
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Book Updated Successfully"
        )

        load_books()

    # Delete Book
    def delete_book():

        selected = tree.focus()

        values = tree.item(
            selected,
            "values"
        )

        if not values:
            messagebox.showerror(
                "Error",
                "Select a book first"
            )
            return

        book_id = values[0]

        confirm = messagebox.askyesno(
            "Confirm",
            "Delete this book?"
        )

        if not confirm:
            return

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM books
            WHERE id=?
            """,
            (book_id,)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Book Deleted Successfully"
        )

        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)

        load_books()

    # Back
    def go_back():

        from pages.dashboard import open_dashboard

        open_dashboard(root)

    # Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(
        btn_frame,
        text="Search",
        command=search_book
    ).pack(side="left", padx=5)

    tk.Button(
        btn_frame,
        text="Refresh",
        command=load_books
    ).pack(side="left", padx=5)

    tk.Button(
        btn_frame,
        text="Update Book",
        command=update_book
    ).pack(side="left", padx=5)

    tk.Button(
        btn_frame,
        text="Delete Book",
        command=delete_book
    ).pack(side="left", padx=5)

    tk.Button(
        btn_frame,
        text="Back",
        command=go_back
    ).pack(side="left", padx=5)

    # Initial Load
    load_books()