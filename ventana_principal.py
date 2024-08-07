from tkinter import*

v=Tk()

v.title("BILLIARD") ##titulo ventana

canvas= Canvas(width = 800, height = 600, bg = 'black')
canvas.pack(expand = YES, fill = BOTH)

#Etiqueta ventana 1
label1 = Label(v, text="jpc97 billiard", bg="black", fg="white")
label1.pack(fill=X, side=TOP)

#Imagen de Fondo
backgroundImage = PhotoImage(file = 'fondo_inicio.png')
canvas.create_image(0, 0, image = backgroundImage, anchor = NW)

#Imagen titulo
##pjImage = PhotoImage(file = 'pj.gif')
##canvas.create_image(130, 50, image = pjImage, anchor = NW)





#Definicion de Funciones

def quit(v):
    v.destroy()    

def funcion():
    quit(v)

    #import colision
    import nombre1jugador

def funcion2():
    quit(v)

    #import colision
    import nombre2jugador    


#Botones Jugar, Salir
jugarImage = PhotoImage(file = 'BOTONES_01.png')
jugarImage2 = PhotoImage(file = 'BOTONES_02.png')
salirImage = PhotoImage(file = 'BOTONES_03.png')
bjugar = Button(v, text = "Jugar", image = jugarImage, command = funcion).place(x=200, y=220)
bjugar = Button(v, text = "Jugar", image = jugarImage2, command = funcion2).place(x=200, y=320)
bsalir = Button(v, text = "Salir", image = salirImage, command = lambda v = v:quit(v)).place(x=200, y=420)

v.mainloop()
