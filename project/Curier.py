from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import re
from tkinter import *
import os, time
import sqlite3
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Студент\Downloads\project\assets\frame3")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

conn = sqlite3.connect('menu.db')
c = conn.cursor()

window = Tk()
window.title("FoodExpress")
window.geometry("689x628")
window.configure(bg = "#222222")
photo = tk.PhotoImage(file='FoodExpress.png')
window.iconphoto(True, photo)


def clear_labels():
    for label in window.place_slaves():
        if isinstance(label, tk.Label):
            label.place_forget()

def delete_data():
    c.execute("DELETE FROM personal ")
    c.execute("DELETE FROM menu")
    conn.commit()
    clear_labels()
    window.destroy()



canvas = Canvas(
    window,
    bg = "#222222",
    height = 628,
    width = 689,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    336.0,
    307.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=delete_data,
    relief="flat"
)
button_1.place(
    x=231.0,
    y=475.0,
    width=207.0,
    height=96.0
)

canvas.create_rectangle(
    14.0,
    77.0,
    654.0,
    78.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    14.0,
    125.0,
    654.0,
    126.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    333.00001525878906,
    77.0,
    334.0000305175781,
    458.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    14.0,
    457.0,
    655.0,
    458.00006103515625,
    fill="#000000",
    outline="")

canvas.create_text(
    198.0,
    26.0,
    anchor="nw",
    text="Вам пришел заказ!",
    fill="#000000",
    font=("Montserrat SemiBold", 28 * -1)
)

canvas.create_text(
    75.0,
    86.0,
    anchor="nw",
    text="Состав заказа:",
    fill="#000000",
    font=("Montserrat SemiBold", 28 * -1)
)

canvas.create_text(
    367.0,
    86.0,
    anchor="nw",
    text="Данные о клиенте",
    fill="#000000",
    font=("Montserrat SemiBold", 24 * -1)
)

c.execute('SELECT id, name FROM menu LIMIT 10')
rows = c.fetchall()

y_place=128
for i, row in enumerate(rows):
    lbl = tk.Label(window, text=f' {row[1]}')
    lbl.config(bg="#FFFFFF",font="Montserrat 15")
    lbl.place(x=22,y=y_place)
    y_place+=33
conn.commit()

c.execute('SELECT id, telephone_number, city, name, address, entrance_and_floor FROM personal LIMIT 6')
rows = c.fetchall()
for i, row in enumerate(rows):
    lbl = tk.Label(window, text=f' {row[1]}\n\n {row[2]}\n\n {row[3]}\n\n {row[4]}\n\n {row[5]}')
    lbl.config(bg="#FFFFFF",font="Montserrat 15")
    lbl.pack(padx=0, pady=15)
    lbl.place(x=335,y=175)
conn.commit()


window.resizable(False, False)
window.mainloop()
