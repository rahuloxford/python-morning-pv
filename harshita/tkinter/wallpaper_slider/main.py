import os
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

counter = 1
def swap_image():
    global counter
    img_label.config(image=imgs[counter % len(imgs)])
    counter += 1

root.title("Wallpaper Slider")
root.geometry("500x550")
root.configure(background="black")

all_imgs = os.listdir("wallpapers")
imgs = []

for img in all_imgs:
    photo = Image.open(os.path.join('wallpapers', img))
    resized_img = photo.resize((400, 300))
    imgs.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image=imgs[0])
img_label.pack(pady=(50, 20))

button = Button(root, text="next image", command=swap_image)
button.pack()
button.config(font=('verdana', 14))

root.mainloop()