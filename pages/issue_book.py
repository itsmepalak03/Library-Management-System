import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime


def issue_book_page(root):

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(
        root,
        text="Issue Book",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    # Book ID
    tk.Label(root, text="Book ID").pack()

    book_entry = tk.Entry(root, width=30)
    book_entry.pack(pady=5)

    # Student ID
    tk.Label(root, text="Student ID").pack()

    student_entry = tk.Entry(root, width=30)
    student_entry.pack(pady=5)

    def issue_book():

        book_id = book_entry.get().strip()
        student_id = student_entry.get().strip()

        if not book_id or not student_id:
            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        # Check Book
        cursor.execute(
            "SELECT quantity FROM books WHERE id=?",
            (book_id,)
        )

        book = cursor.fetchone()

        if not book:
            messagebox.showerror(
                "Error",
                "Book ID not found"
            )
            conn.close()
            return

        quantity = book[0]

        if quantity <= 0:
            messagebox.showerror(
                "Error",
                "Book Out Of Stock"
            )
            conn.close()
            return

        # Check Student
        cursor.execute(
            "SELECT * FROM students WHERE id=?",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:
            messagebox.showerror(
                "Error",
                "Student ID not found"
            )
            conn.close()
            return

        # Insert Issue Record
        issue_date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute(
            """
            INSERT INTO issued_books
            (book_id, student_id, issue_date)
            VALUES (?, ?, ?)
            """,
            (book_id, student_id, issue_date)
        )

        # Reduce Quantity
        cursor.execute(
            """
            UPDATE books
            SET quantity = quantity - 1
            WHERE id = ?
            """,
            (book_id,)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Book Issued Successfully"
        )

        book_entry.delete(0, tk.END)
        student_entry.delete(0, tk.END)

    def go_back():
        from pages.dashboard import open_dashboard
        open_dashboard(root)

    tk.Button(
        root,
        text="Issue Book",
        width=20,
        command=issue_book
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back",
        width=20,
        command=go_back
    ).pack(pady=5)