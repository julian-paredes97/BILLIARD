from tkinter import*

v=Tk()

v.title("BILLIARD") ##titulo ventana
##v.geometry("800x566")
v.configure(bg="black")

canvas= Canvas(width = 500, height = 200, bg = 'black')
label1=Label(v,text="ingrese el nombre del 1 jugador:")
entry1=Entry(v, text="")


label1.grid(row=0)
entry1.grid(row=1,column=0)

label2=Label(v,text="ingrese el nombre del 2 jugador:")
entry2=Entry(v, text="")
##
label2.grid(row=0,column=1)
entry2.grid(row=1,column=1)
##label2=Label(v,text="ingrese el nombre del 2 jugador:")
####entry2=Entry(v, text="")
####
##label2.grid(row=600)
##entry2.grid(row=500,column=0,sticky=E)
canvas.grid()
##label2=Label(v,text="ingrese el nombre del 2 jugador:")
##entry2=Entry(v, text="")
####
##label2.grid(row=0,column=1)
##entry2.grid(row=1,column=1)


##label1=Label(v,text="ingrese el nombre del jugador:")
##entry1=Entry(v)
##
##label1.grid(row=0)
##entry1.grid(row=0,column=1)



def save(entry1):

    print(text)
##    entry1.readline()
##    f=open("juegasolo.txt",mode='w')
##
##    f.write(entry1)
    

def quit(v):
    v.destroy()    

def funcion():
    quit(v)

    #import billar
    import billar3



bjugar = Button(v, text = "GUARDAR NOMBRES", command = funcion).place(x=300, y=70)



v.mainloop()
