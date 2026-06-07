import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Books Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
""")

# Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL
)
""")

# Issued Books Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books(
    issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    student_id INTEGER,
    issue_date TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")