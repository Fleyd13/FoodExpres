from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sqlite3
from tkinter import *
import os, time
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Студент\Downloads\project\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_file():
    file_path = r"C:\Users\Студент\Downloads\project\Cart.py"
    os.system(file_path)

conn = sqlite3.connect('menu.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS menu
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER)''')
conn.commit()

def button_1_add():
    name = "Безумный Бургер"
    price = 500
    cursor.execute("INSERT INTO menu (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    print("Button clicked and data added to the database.")

def button_2_add():
    name = "Паста Карбонара"
    price = 850
    cursor.execute("INSERT INTO menu (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    print("Button clicked and data added to the database.")

def button_3_add():
    name = "Ролл Рио"
    price = 499
    cursor.execute("INSERT INTO menu (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    print("Button clicked and data added to the database.")

def button_4_add():
    name = "Баварская Пицца"
    price = 700
    cursor.execute("INSERT INTO menu (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    print("Button clicked and data added to the database.")

def button_5_add():
    name = "Картошка Фри"
    price = 120
    cursor.execute("INSERT INTO menu (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    print("Button clicked and data added to the database.")

def button_7_add():
    name = "Ламаджо"
    price = 250
    cursor.execute("INSERT INTO menu (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    print("Button clicked and data added to the database.")

window = Tk()
window.title("FoodExpress")
window.geometry("802x838")
window.configure(bg = "#FFFFFF")
photo = tk.PhotoImage(file='FoodExpress.png')
window.iconphoto(True, photo)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 838,
    width = 802,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    409.0,
    439.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    401.0,
    456.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    642.0,
    274.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    162.0,
    273.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    398.0,
    276.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    401.0,
    636.0,
    image=image_image_6
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_1_add(), 
    relief="flat", 
    name="burger"
)


button_1.place(
    x=56.0,
    y=400.0,
    width=207.0,
    height=34.88571548461914
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_2_add(),
    relief="flat"
)
button_2.place(
    x=295.0,
    y=400.0,
    width=207.0,
    height=34.88571548461914
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    643.0,
    636.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    158.0,
    636.0,
    image=image_image_8
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_3_add(),
    relief="flat"
)
button_3.place(
    x=57.0,
    y=758.0,
    width=207.0,
    height=34.885711669921875
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_4_add(),
    relief="flat"
)
button_4.place(
    x=299.0,
    y=758.0,
    width=207.0,
    height=34.885711669921875
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_5_add(),
    relief="flat"
)
button_5.place(
    x=543.0,
    y=758.0,
    width=207.0,
    height=34.885711669921875
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    731.0,
    36.0,
    image=image_image_9
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command= open_file,
    relief="flat"
)
button_6.place(
    x=712.5,
    y=19.0,
    width=33.0,
    height=33.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_7_add(),
    relief="flat"
)
button_7.place(
    x=536.0,
    y=400.0,
    width=207.0,
    height=34.88571548461914
)
window.resizable(False, False)
window.mainloop()
