from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sqlite3
import tkinter as tk
from tkinter import *
import os, time
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Студент\Downloads\project\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def register():
    username = entry_1.get()
    password = entry_2.get()
    c.execute("SELECT username, password FROM users WHERE username = ? AND password = ?", (username, password))
    if c.fetchone() is None:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        db.commit()
        register_label.config(text="Вы зарегистрировались!")
    else:
        register_label.config(text="Учётная запись уже существует")
        return

def login():
    username = entry_1.get()
    password = entry_2.get()
    c.execute("SELECT username, password FROM users WHERE username = ? AND password = ?", (username, password))

    if c.fetchone() is not None:
        register_label.config(text="Добро пожаловать!")
        window.destroy()
        os.system(r'C:\Users\Студент\Downloads\project\Main_menu.py')
    else:
        register_label.config(text="Неверные учётные данные")

window = Tk()
window.title("FoodExpress")
window.geometry("803x602")
window.configure(bg = "#FFFFFF")
photo = tk.PhotoImage(file='FoodExpress.png')
window.iconphoto(True, photo)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 602,
    width = 803,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    401.0,
    301.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    402.0,
    301.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    394.6287384033203,
    294.9096221923828,
    image=entry_image_1
)
entry_1 = Entry(
    show="*",
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=285.9096221923828,
    y=265.0,
    width=217.438232421875,
    height=57.819244384765625
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    391.6287384033203,
    208.9096221923828,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=282.9096221923828,
    y=179.0,
    width=217.438232421875,
    height=57.819244384765625
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=register,
    relief="flat"
)
button_1.place(
    x=343.0,
    y=427.0,
    width=104.4462890625,
    height=41.778533935546875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_2.place(
    x=343.0,
    y=371.0,
    width=104.4462890625,
    height=41.778533935546875
)

canvas.create_text(
    276.0,
    159.0,
    anchor="nw",
    text="Login:",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 12 * -1)
)

canvas.create_text(
    276.0,
    244.0,
    anchor="nw",
    text="Password:",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 12 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    401.0,
    138.0,
    image=image_image_3
)

canvas.create_text(
    327.0,
    334.0,
    anchor="nw",
    text="  ",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 12 * -1)
)

db = sqlite3.connect('data.db')
c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS "users" (
    "username"  TEXT,
    "password"  TEXT)""")
db.commit()

register_label = tk.Label(window, text="",background='#333333',foreground='#FFFFFF')
register_label.place(x=325.0,y=340)

window.resizable(False, False)
window.mainloop()