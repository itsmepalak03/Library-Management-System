import tkinter as tk
import sqlite3

from pages.add_book import add_book_page
from pages.view_books import view_books_page
from pages.students import students_page
from pages.issue_book import issue_book_page
from pages.return_book import return_book_page
from pages.issued_books import issued_books_page
from pages.report import export_report

FONT_TITLE = ("Arial", 22, "bold")
FONT_CARD = ("Arial", 14, "bold")
FONT_BUTTON = ("Arial", 11, "bold")


def open_dashboard(root):

    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#f4f6f9")

    # Header
    header = tk.Frame(root, bg="#2C3E50", height=80)
    header.pack(fill="x")

    tk.Label(
        header,
        text="Library Management System",
        font=FONT_TITLE,
        fg="white",
        bg="#2C3E50"
    ).pack(pady=20)

    # Welcome Message
    tk.Label(
        root,
        text="Welcome Admin",
        font=("Arial", 14),
        bg="#f4f6f9",
        fg="#34495E"
    ).pack(pady=10)

    # Statistics
    try:
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM books")
        total_books = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM students")
        total_students = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM issued_books")
        total_issued = cursor.fetchone()[0]

        conn.close()

    except Exception:
        total_books = 0
        total_students = 0
        total_issued = 0

    stats_frame = tk.Frame(root, bg="#f4f6f9")
    stats_frame.pack(pady=15)

    tk.Label(
        stats_frame,
        text=f"📚\nTotal Books\n{total_books}",
        font=FONT_CARD,
        bg="#D6EAF8",
        relief="raised",
        bd=2,
        width=18,
        height=5
    ).grid(row=0, column=0, padx=15)

    tk.Label(
        stats_frame,
        text=f"👨‍🎓\nStudents\n{total_students}",
        font=FONT_CARD,
        bg="#D5F5E3",
        relief="raised",
        bd=2,
        width=18,
        height=5
    ).grid(row=0, column=1, padx=15)

    tk.Label(
        stats_frame,
        text=f"📖\nIssued Books\n{total_issued}",
        font=FONT_CARD,
        bg="#FADBD8",
        relief="raised",
        bd=2,
        width=18,
        height=5
    ).grid(row=0, column=2, padx=15)

    # Buttons Frame
    button_frame = tk.Frame(root, bg="#f4f6f9")
    button_frame.pack(pady=20)

    # Row 1
    tk.Button(
        button_frame,
        text="Add Book",
        width=20,
        height=2,
        bg="#27AE60",
        fg="white",
        font=FONT_BUTTON,
        command=lambda: add_book_page(root)
    ).grid(row=0, column=0, padx=10, pady=10)

    tk.Button(
        button_frame,
        text="View Books",
        width=20,
        height=2,
        bg="#3498DB",
        fg="white",
        font=FONT_BUTTON,
        command=lambda: view_books_page(root)
    ).grid(row=0, column=1, padx=10, pady=10)

    tk.Button(
        button_frame,
        text="Students",
        width=20,
        height=2,
        bg="#F39C12",
        fg="white",
        font=FONT_BUTTON,
        command=lambda: students_page(root)
    ).grid(row=0, column=2, padx=10, pady=10)

    # Row 2
    tk.Button(
        button_frame,
        text="Issue Book",
        width=20,
        height=2,
        bg="#9B59B6",
        fg="white",
        font=FONT_BUTTON,
        command=lambda: issue_book_page(root)
    ).grid(row=1, column=0, padx=10, pady=10)

    tk.Button(
        button_frame,
        text="Return Book",
        width=20,
        height=2,
        bg="#E67E22",
        fg="white",
        font=FONT_BUTTON,
        command=lambda: return_book_page(root)
    ).grid(row=1, column=1, padx=10, pady=10)

    tk.Button(
        button_frame,
        text="Issued Books",
        width=20,
        height=2,
        bg="#16A085",
        fg="white",
        font=FONT_BUTTON,
        command=lambda: issued_books_page(root)
    ).grid(row=1, column=2, padx=10, pady=10)

    # Logout Function
    def logout():
        from pages.login import login

        for widget in root.winfo_children():
            widget.destroy()

        login(root)

    # Row 3
    tk.Button(
        button_frame,
        text="Export Report",
        width=20,
        height=2,
        bg="#2ECC71",
        fg="white",
        font=FONT_BUTTON,
        command=export_report
    ).grid(row=2, column=0, padx=10, pady=10)

    tk.Button(
        button_frame,
        text="Logout",
        width=20,
        height=2,
        bg="#7F8C8D",
        fg="white",
        font=FONT_BUTTON,
        command=logout
    ).grid(row=2, column=1, padx=10, pady=10)

    tk.Button(
        button_frame,
        text="Exit",
        width=20,
        height=2,
        bg="#E74C3C",
        fg="white",
        font=FONT_BUTTON,
        command=root.destroy
    ).grid(row=2, column=2, padx=10, pady=10)

    # Row 4
    tk.Button(
        button_frame,
        text="Refresh Dashboard",
        width=20,
        height=2,
        bg="#2980B9",
        fg="white",
        font=FONT_BUTTON,
        command=lambda: open_dashboard(root)
    ).grid(row=3, column=1, padx=10, pady=10)

    # Footer
    footer = tk.Label(
        root,
        text="Library Management System © 2026",
        bg="#2C3E50",
        fg="white",
        font=("Arial", 10)
    )

    footer.pack(side="bottom", fill="x")
