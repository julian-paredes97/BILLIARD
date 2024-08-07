from tkinter import*
import tkinter as tk
import time
import math
import random

class Bola:
    def __init__(self, canvas, x, y, radio, color, numero):
        self.canvas = canvas
        self.radio = radio
        self.color = color
        self.numero = numero
        self.x = x
        self.y = y
        self.dx = random.choice([-2, 2])
        self.dy = random.choice([-2, 2])
        # self.dx = 0
        # self.dy = 0
        self.id = canvas.create_oval(self.x - radio, self.y - radio, self.x + radio, self.y + radio, fill=color)
        self.text_id = canvas.create_text(self.x, self.y, text=str(self.numero), fill="white")

    def mover(self):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radio <= 0 or self.x + self.radio >= self.canvas.winfo_width():
            self.dx = -self.dx
        if self.y - self.radio <= 0 or self.y + self.radio >= self.canvas.winfo_height():
            self.dy = -self.dy

        self.canvas.move(self.id, self.dx, self.dy)
        self.canvas.move(self.text_id, self.dx, self.dy)

    def colision(self, otra_bola):
        dist = ((self.x - otra_bola.x) ** 2 + (self.y - otra_bola.y) ** 2) ** 0.5
        return dist <= self.radio + otra_bola.radio


def actualizar():
    for bola in bolas:
        bola.mover()

    for i in range(len(bolas)):
        for j in range(i + 1, len(bolas)):
            if bolas[i].colision(bolas[j]):
                bolas[i].dx, bolas[j].dx = bolas[j].dx, bolas[i].dx
                bolas[i].dy, bolas[j].dy = bolas[j].dy, bolas[i].dy
    
    root.after(20, actualizar)

root = tk.Tk()
#root.title("Colisiones de Bolas")
root.title("billar")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas=Canvas(root,width=800,height=556,bd=0,highlightthickness=0)
imagen_fondo=PhotoImage(file="billar_julian2.png")  ##imagen fondo canvas
canvas.create_image(400,280,image=imagen_fondo)     ## cambiar pos img bg


#canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

bolas = []
#colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta", "lime", "pink", "brown", "gray", "violet", "turquoise", "gold"]
colors = ['yellow2','blue','red','purple','orangered','green','brown','black','yellow4','blue2','red2','purple2','darkorange','green2','darkred']


Xcords = [480,500,500,520,520,520,540,540,540,540,560,560,560,560,560]
Ycords = [250,240,260,230,250,270,220,240,260,280,210,230,250,270,290]


for i in range(15):
    x = Xcords[i]
    y = Ycords[i]
    # x = random.randint(20, 580)
    # y = random.randint(20, 380)
    radio = 10
    color = colors[i] #random.choice(colors)
    bola = Bola(canvas, x, y, radio, color, i + 1)
    bolas.append(bola)




actualizar()

root.mainloop()
