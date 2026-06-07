import tkinter as tk
from tkinter import messagebox
import sqlite3


def return_book_page(root):

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(
        root,
        text="Return Book",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(root, text="Issue ID").pack()

    issue_entry = tk.Entry(root, width=30)
    issue_entry.pack(pady=5)

    def return_book():

        issue_id = issue_entry.get().strip()

        if issue_id == "":
            messagebox.showerror(
                "Error",
                "Enter Issue ID"
            )
            return

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        # Find Issue Record
        cursor.execute(
            """
            SELECT book_id
            FROM issued_books
            WHERE issue_id=?
            """,
            (issue_id,)
        )

        record = cursor.fetchone()

        if not record:
            messagebox.showerror(
                "Error",
                "Issue ID Not Found"
            )
            conn.close()
            return

        book_id = record[0]

        # Increase Quantity
        cursor.execute(
            """
            UPDATE books
            SET quantity = quantity + 1
            WHERE id=?
            """,
            (book_id,)
        )

        # Delete Issue Record
        cursor.execute(
            """
            DELETE FROM issued_books
            WHERE issue_id=?
            """,
            (issue_id,)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Book Returned Successfully"
        )

        issue_entry.delete(0, tk.END)

    def go_back():
        from pages.dashboard import open_dashboard
        open_dashboard(root)

    tk.Button(
        root,
        text="Return Book",
        width=20,
        command=return_book
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back",
        width=20,
        command=go_back
    ).pack(pady=5)