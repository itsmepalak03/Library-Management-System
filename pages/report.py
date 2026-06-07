import csv
import sqlite3
from tkinter import messagebox


def export_report():

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    with open("library_report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # Books
        writer.writerow(["BOOKS"])
        writer.writerow(["ID", "Title", "Author", "Quantity"])

        cursor.execute("SELECT * FROM books")

        for row in cursor.fetchall():
            writer.writerow(row)

        writer.writerow([])

        # Students
        writer.writerow(["STUDENTS"])
        writer.writerow(["ID", "Name", "Course"])

        cursor.execute("SELECT * FROM students")

        for row in cursor.fetchall():
            writer.writerow(row)

        writer.writerow([])

        # Issued Books
        writer.writerow(["ISSUED BOOKS"])
        writer.writerow([
            "Issue ID",
            "Book ID",
            "Student ID",
            "Issue Date"
        ])

        cursor.execute("SELECT * FROM issued_books")

        for row in cursor.fetchall():
            writer.writerow(row)

    conn.close()

    messagebox.showinfo(
        "Success",
        "Report Exported Successfully"
    )