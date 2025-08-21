# Tkinter is Python's standard library for creating Graphical User Interfaces (GUIs).

from tkinter import *
import os

root = Tk()

root.title("My App")

# root.minsize(450, 320)
# root.maxsize(750, 500)

root.geometry("500x600")
root.configure(background="aqua")
icon = os.path.join(os.path.dirname(__file__), "logo.ico")
root.iconbitmap(icon)

root.mainloop()