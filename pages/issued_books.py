import tkinter as tk
from tkinter import ttk
import sqlite3


def issued_books_page(root):

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(
        root,
        text="Issued Books",
        font=("Arial", 20, "bold")
    ).pack(pady=10)

    columns = (
        "Issue ID",
        "Book ID",
        "Student ID",
        "Issue Date"
    )

    tree = ttk.Treeview(
        root,
        columns=columns,
        show="headings",
        height=15
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(pady=10)

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM issued_books")

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        tree.insert("", tk.END, values=row)

    def go_back():
        from pages.dashboard import open_dashboard
        open_dashboard(root)

    tk.Button(
        root,
        text="Back",
        command=go_back
    ).pack(pady=10)