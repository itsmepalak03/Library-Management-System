import tkinter as tk
from pages.login import login

# Create Window
root = tk.Tk()

# Title
root.title("Library Management System")

# Window Size
window_width = 1000
window_height = 650

# Center Window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Prevent very small resizing
root.minsize(900, 600)

# Background Color
root.configure(bg="#f5f5f5")

# Optional Icon
# Uncomment if you have assets/icon.ico
# root.iconbitmap("assets/icon.ico")

# Launch Login Page
login(root)

# Start Application
root.mainloop()