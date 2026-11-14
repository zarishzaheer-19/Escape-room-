
import tkinter as tk

# Create main window
window = tk.Tk()

# Window settings
window.title("THE LAST CLUE")
window.geometry("800x500")
window.configure(bg="#1c2433")

# Game title
title = tk.Label(
    window,
    text="THE LAST CLUE",
    font=("Arial", 30, "bold"),
    fg="white",
    bg="#1c2433"
)
title.pack(pady=80)

# Welcome message
welcome = tk.Label(
    window,
    text="Welcome, Detective!",
    font=("Arial", 18),
    fg="lightgray",
    bg="#1c2433"
)
welcome.pack(pady=10)

# Start button
start_button = tk.Button(
    window,
    text="START GAME",
    font=("Arial", 14),
    width=18
)
start_button.pack(pady=30)

# Run the window
window.mainloop()
