import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def students_page(root):

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(
        root,
        text="Student Management",
        font=("Arial", 20, "bold")
    ).pack(pady=10)

    # Name
    tk.Label(root, text="Student Name").pack()

    name_entry = tk.Entry(root, width=40)
    name_entry.pack(pady=5)

    # Course
    tk.Label(root, text="Course").pack()

    course_entry = tk.Entry(root, width=40)
    course_entry.pack(pady=5)

    # Table
    columns = ("ID", "Name", "Course")

    tree = ttk.Treeview(
        root,
        columns=columns,
        show="headings",
        height=10
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200)

    tree.pack(pady=10)

    def load_students():

        tree.delete(*tree.get_children())

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")

        rows = cursor.fetchall()

        conn.close()

        for row in rows:
            tree.insert("", tk.END, values=row)

    def add_student():

        name = name_entry.get().strip()
        course = course_entry.get().strip()

        if name == "":
            messagebox.showerror("Error", "Enter Student Name")
            return

        if course == "":
            messagebox.showerror("Error", "Enter Course")
            return

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO students(name, course)
            VALUES (?, ?)
            """,
            (name, course)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Student Added Successfully"
        )

        name_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)

        load_students()

    def go_back():
        from pages.dashboard import open_dashboard
        open_dashboard(root)

    tk.Button(
        root,
        text="Add Student",
        command=add_student
    ).pack(pady=5)

    tk.Button(
        root,
        text="Back",
        command=go_back
    ).pack(pady=5)

    load_students()