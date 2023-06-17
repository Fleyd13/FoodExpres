from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,ttk
import re
from tkinter import *
import os, time
import sqlite3
import tkinter as tk
 
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Студент\Downloads\project\assets\frame2")
 
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
 
def save_to_database():
    telephone_number = entry_1.get()
    city = entry_2.get()
    name = entry_3.get()
    address = entry_4.get()
    entrance_floor = entry_5.get()
    c.execute("""INSERT INTO personal (
    telephone_number, city, name, address, entrance_and_floor) 
    VALUES (?, ?, ?, ?, ?)""", (telephone_number, city, name, address, entrance_floor))
    conn.commit()
    conn.close()    

conn = sqlite3.connect('menu.db')
c = conn.cursor()
 
c.execute("""CREATE TABLE IF NOT EXISTS personal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telephone_number TEXT,
    city TEXT,
    name TEXT,
    address TEXT,
    entrance_and_floor TEXT)""")
 
c.execute('SELECT id, name, price FROM menu LIMIT 10')
rows = c.fetchall()
 
result = c.execute('SELECT id, price FROM menu LIMIT 10')
total_price = 0
for row in result:
    total_price += row[1]
 
window = Tk()
window.title("FoodExpress")
 
def is_valid(newval):
    return re.match("^\+\d{0,11}$", newval) is not None
 
window.geometry("953x857")
window.configure(bg = "#222222")
 
check = (window.register(is_valid), "%P")
canvas = Canvas(
    window,
    bg = "#222222",
    height = 857,
    width = 953,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
 
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    473.0,
    541.0,
    image=image_image_1
)
 
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    473.0,
    598.0,
    image=image_image_2
)
 
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    473.0,
    655.0,
    image=image_image_3
)
 
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    473.0,
    712.0,
    image=image_image_4
)
 
image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    473.0,
    234.0,
    image=image_image_5
)
 
image_image_8 = PhotoImage(
file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
630.0,
81.0,
image=image_image_8
)
 
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    comman=lambda: [save_to_database(),clear_labels()],
    relief="flat"
)
 
button_1.place(
    x=373.0,
    y=745.0,
    width=207.0,
    height=96.0
)
 
image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    473.0,
    484.0,
    image=image_image_7
)
 
 
 
image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    530.0,
    425.0,
    image=image_image_10
)
 
canvas.create_rectangle(
    495.0,
    102.0,
    826.3739318847656,
    103.0,
    fill="#A5A5A5",
    outline="")
 
canvas.create_rectangle(
    496.0,
    408.0,
    827.3739318847656,
    409.0,
    fill="#A5A5A5",
    outline="")
 
image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    276.0,
    235.0,
    image=image_image_13
)
 
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    570.5,
    485.0,
    image=entry_image_1
)
entry_1 = Entry(
    validate="key",
    font=("Montserrat 14"),
    validatecommand=check,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
 
entry_1.place(
    x=271.0,
    y=471.0,
    width=599.0,
    height=26.0
)
 
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    511.0,
    542.0,
    image=entry_image_2
)
entry_2 = Entry(
    font=("Montserrat 14"),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=152.0,
    y=528.0,
    width=718.0,
    height=26.0
)
 
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    509.0,
    599.0,
    image=entry_image_3
)
entry_3 = Entry(
    font=("Montserrat 14"),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=148.0,
    y=585.0,
    width=722.0,
    height=26.0
)
 
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    515.5,
    655.0,
    image=entry_image_4
)
entry_4 = Entry(
    font=("Montserrat 14"),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=161.0,
    y=641.0,
    width=709.0,
    height=26.0
)
 
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    562.5,
    713.0,
    image=entry_image_5
)
entry_5 = Entry(
    font=("Montserrat 14"),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=255.0,
    y=699.0,
    width=615.0,
    height=26.0
)
 
total_price_label = tk.Label(window, text=f"{total_price}₽")
total_price_label.place(x=565,y=411)
total_price_label.config(bg="#FFFFFF",font="Montserrat 16")
 
y_place=105
for i, row in enumerate(rows):
    lbl = tk.Label(window, text=f' {row[1]} \t\t {row[2]}₽ ')
    lbl.config(bg="#FFFFFF",font="Montserrat 16")
    lbl.place(x=488,y=y_place)
    y_place+=30
 


def clear_labels():
    for label in window.place_slaves():
        if isinstance(label, tk.Label):
            label.place_forget()
 
 
window.resizable(False, False)
window.mainloop()