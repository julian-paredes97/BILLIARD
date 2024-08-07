from tkinter import*

v=Tk()

v.title("BILLIARD") ##titulo ventana
##v.geometry("800x566")
v.configure(bg="black")

canvas= Canvas(width = 400, height = 200, bg = 'black')
label1=Label(v,text="ingrese el nombre del jugador:")
entry1=Entry(v, text="")

label1.grid()
entry1.grid(row=100,column=0)
canvas.grid()

##label1=Label(v,text="ingrese el nombre del jugador:")
##entry1=Entry(v)
##
##label1.grid(row=0)
##entry1.grid(row=0,column=1)



def save(entry1):
    entry1 = ""
    f=open("juegasolo.txt",mode='w')

    f.write(entry1)

    f.close()
    

def quit(v):
    v.destroy()    

def funcion():
    quit(v)

    #import billar
    import billar2



bguardar = Button(v, text = "guardar", command = funcion).place(x=175, y=50)



v.mainloop()
