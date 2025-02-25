import os
from tkinter import *
from tkinter import filedialog
import  tkinter as tk
from PIL import Image, ImageTk

def showImage():
    file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(("JPG File", "*.jpg"),("PNG file", "*.png"), ("All file", "how are you . txt")))
    img = Image.open(file_name)
    img = img.resize((300, 300)) #ปรับขนาดภาพ
    img = ImageTk.PhotoImage(img)
    lbl.image = img #เก็บอ้างอิง
    lbl.configure(image=img) #แสดงรูปภาพ

root = Tk()

frame = Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frame, text="Select Image", command=showImage)
btn.pack(side=tk.LEFT)

btn2 = Button(frame, text="Exit", command=lambda:exit())
btn2.pack(side=tk.LEFT, padx=12)


root.title("Image Viewer")
root.geometry("400x450")
root.mainloop()

