#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 20:08:49 2022

@author: priyankadas
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Canvas")
root.geometry("1000x600")

colour = Label(root, text = "Enter a colour")
colour.place(relx = 0.6, rely = 0.9, anchor = CENTER)

input1 = Entry(root)
input1.insert(0, "black")
input1.place(relx = 0.8, rely = 0.9, anchor = CENTER)

canvas = Canvas(root, width = 1000, height = 500, bg = "white", highlightbackground = "lightgray")
canvas.pack()

#img = ImageTk.PhotoImage(Image.open("start_point1.png"))
#my_img = canvas.create_image(50, 50, image = img)

fill_colour = ["Green", "Yellow", "Orange","Red" ]

colour_dropdown = ttk.Combobox(root, values = fill_colour, state = "readonly", width = 10)
colour_dropdown.place(relx = 0.8, rely = 0.9, anchor = CENTER)

startx = Label(root, text = "Startx")
startx.place(relx = 0.1, rely = 0.85, anchor = CENTER)
starty = Label(root, text = "Starty")
starty.place(relx = 0.3, rely = 0.85, anchor = CENTER)
endx = Label(root, text = "Endx")
endx.place(relx = 0.5, rely = 0.85, anchor = CENTER)
endy = Label(root, text = "Endy")
endy.place(relx = 0.7, rely = 0.85, anchor = CENTER)

values = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900]

d1 = ttk.Combobox(root, values = values, state = "readonly", width = 10)
d1.place(relx = 0.2, rely = 0.85, anchor = CENTER)

d2 = ttk.Combobox(root, values = values, state = "readonly", width = 10)
d2.place(relx = 0.4, rely = 0.85, anchor = CENTER)

d3 = ttk.Combobox(root, values = values, state = "readonly", width = 10)
d3.place(relx = 0.6, rely = 0.85, anchor = CENTER)

d4 = ttk.Combobox(root, values = values, state = "readonly", width = 10)
d4.place(relx = 0.8, rely = 0.85, anchor = CENTER)

def right_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx+5
    direction = "Right"
    draw(direction, oldx, oldy, newx, newy)
    
def left_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx-5
    direction = "Left"
    draw(direction, oldx, oldy, newx, newy)
    
def up_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy-5
    direction = "Up"
    draw(direction, oldx, oldy, newx, newy)
    
def down_dir(event):
    global oldx
    global oldy
    global newx 
    global newy
    oldx = newx
    oldy = newy
    newy = newy+5
    direction = "Down"
    draw(direction, oldx, oldy, newx, newy)
    
def draw(direction, oldx, oldy, newx, newy):
    fill_colour = input1.get()
    if(direction == "Right"):
        r_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = fill_colour)
        
    if(direction == "Left"):
        l_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = fill_colour)
        
    if(direction == "Up"):
        u_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = fill_colour)
        
    if(direction == "Down"):
        d_line = canvas.create_line(oldx, oldy, newx, newy, width = 3, fill = fill_colour)
    
root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)


root.mainloop()