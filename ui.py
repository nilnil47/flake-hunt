import tkinter as tk
from tkinter import colorchooser

# create a tkinter window
root = tk.Tk()

# function to choose a color from the color palette
def choose_color():
    color = colorchooser.askcolor(title="Choose a color")
    # update the background color of the tkinter window to the selected color
    print(color)
    root.configure(background=color[1])

# create a button to choose a color
button = tk.Button(root, text="Choose a color", command=choose_color)
button.pack()

# start the tkinter event loop
root.mainloop()
