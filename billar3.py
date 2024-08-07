from tkinter import*
import random
import time
import math


class Pelota:
    def __init__(self,canvas,palo,paalo2,puntuacion,color):
        self.canvas= canvas
        self.palo= palo
        self.palo2=palo2
        self.puntuacion=puntuacion
        self.id= canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,270,250)
        self.x=0    #cambia dir pelota
        self.y=0    #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()



    def golpea_palo(self,pos):
        palo_pos=self.canvas.coords(self.palo.id)
        if pos[2] >= palo_pos[0] and pos[0] <= palo_pos[2]:  #contacto-x
            if pos[3] >= palo_pos[1] and pos[1] <=palo_pos[3]:  #contacto-y
                #self.puntuacion.tanto()    # formula puntuacion
                return True
        return False
    
    def golpea_palo2(self,pos):
        palo2_pos=self.canvas.coords(self.palo2.id)
        if pos[2] >= palo2_pos[0] and pos[0] <= palo2_pos[2]:  #contacto-x
            if pos[3] >= palo2_pos[1] and pos[1] <=palo2_pos[3]:  #contacto-y
                #self.puntuacion.tanto()    # formula puntuacion
                return True
        return False


     

    
        

    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

        
        if pos[1]<=140:                   # donde rebota arriba y
            self.y=1
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_palo(pos)==True:
            self.x=3
            self.y=0.2

        if self.golpea_palo2(pos)==True:
            self.x=3
            self.y=0.2    

##        if (pos[3]= self.canvas_height-100) and (pos[2]>= self.canvas_width-90):
##            pos[2]>= self.canvas_width-90


          

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1
            #self.puntuacion.tanto()

                        
class Bola1:                                #crea bola 1
    def __init__(self,canvas,pelota,color):
        self.canvas= canvas
        self.pelota= pelota
        self.id = canvas.create_oval(10,10,25,25,fill=color)
##        self.t=canvas.create_text(250,452,text="1",fill="white")
        self.canvas.move(self.id,480,250)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def quit(Bola1,pos):
            Bola1.destroy() 


    def dibujar(self):
##        self.t=canvas.create_text(300,200,text="1",fill='white')

        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota 
        pos= self.canvas.coords(self.id)
        #print(pos)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=0.8

##        if pos[1] and pos[3] and pos[2] and pos[0] =    

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1




class Bola2:                                #crea bola 2
    def __init__(self,canvas,pelota,B1,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,500,240)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1



class Bola3:                                #crea bola 3
    def __init__(self,canvas,pelota,B1,B2,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,500,260)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False
    


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=-0.2
            

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1



class Bola4:                                #crea bola 4
    def __init__(self,canvas,pelota,B1,B2,B3,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3=B3
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,520,230)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False
    


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=-1
                      

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1
            
class Bola5:                                #crea bola 5
    def __init__(self,canvas,pelota,B1,B2,B3,B4,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,520,250)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False
    


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=-0.5    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
    

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=1        
            

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1


class Bola6:                                #crea bola 6
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,520,270)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False
    


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=0.5    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B5(pos) == True:
            self.x=1
            self.y=0.5      
            

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1



class Bola7:                                #crea bola 7
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,B6,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.B6= B6
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,540,220)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False

    def golpea_B6(self,pos):
        B6_pos=self.canvas.coords(self.B6.id)
        if pos[2] >= B6_pos[0] and pos[0] <= B6_pos[2]:
            if pos[3] >= B6_pos[1] and pos[3] <= B6_pos[3]:
                return True
        return False
    


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=-1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=-0.5

        if self.golpea_B5(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B6(pos) == True:
            self.x=1
            self.y=1       
            

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1


class Bola8:                                #crea bola 8
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,B6,B7,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.B6= B6
        self.B7= B7
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,540,240)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False

    def golpea_B6(self,pos):
        B6_pos=self.canvas.coords(self.B6.id)
        if pos[2] >= B6_pos[0] and pos[0] <= B6_pos[2]:
            if pos[3] >= B6_pos[1] and pos[3] <= B6_pos[3]:
                return True
        return False

    def golpea_B7(self,pos):
        B7_pos=self.canvas.coords(self.B7.id)
        if pos[2] >= B7_pos[0] and pos[0] <= B7_pos[2]:
            if pos[3] >= B7_pos[1] and pos[3] <= B7_pos[3]:
                return True
        return False
    


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=-0.2    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=-1
            self.y=-1

        if self.golpea_B5(pos) == True:
            self.x=1
            self.y=-0.2

        if self.golpea_B6(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B7(pos) == True:
            self.x=1
            self.y=1  
            

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1                     
            
class Bola9:                                #crea bola 9
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.B6= B6
        self.B7= B7
        self.B8= B8
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,540,260)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False

    def golpea_B6(self,pos):
        B6_pos=self.canvas.coords(self.B6.id)
        if pos[2] >= B6_pos[0] and pos[0] <= B6_pos[2]:
            if pos[3] >= B6_pos[1] and pos[3] <= B6_pos[3]:
                return True
        return False

    def golpea_B7(self,pos):
        B7_pos=self.canvas.coords(self.B7.id)
        if pos[2] >= B7_pos[0] and pos[0] <= B7_pos[2]:
            if pos[3] >= B7_pos[1] and pos[3] <= B7_pos[3]:
                return True
        return False

    def golpea_B8(self,pos):
        B8_pos=self.canvas.coords(self.B8.id)
        if pos[2] >= B8_pos[0] and pos[0] <= B8_pos[2]:
            if pos[3] >= B8_pos[1] and pos[3] <= B8_pos[3]:
                return True
        return False
    


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B5(pos) == True:
            self.x=0.7
            self.y=0.5

        if self.golpea_B6(pos) == True:
            self.x=1
            self.y=-0.5

        if self.golpea_B7(pos) == True:
            self.x=1
            self.y=1
            
        if self.golpea_B8(pos) == True:
            self.x=1
            self.y=1     
            

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1


class Bola10:                                #crea bola 10
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.B6= B6
        self.B7= B7
        self.B8= B8
        self.B9= B9
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,540,280)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False

    def golpea_B6(self,pos):
        B6_pos=self.canvas.coords(self.B6.id)
        if pos[2] >= B6_pos[0] and pos[0] <= B6_pos[2]:
            if pos[3] >= B6_pos[1] and pos[3] <= B6_pos[3]:
                return True
        return False

    def golpea_B7(self,pos):
        B7_pos=self.canvas.coords(self.B7.id)
        if pos[2] >= B7_pos[0] and pos[0] <= B7_pos[2]:
            if pos[3] >= B7_pos[1] and pos[3] <= B7_pos[3]:
                return True
        return False

    def golpea_B8(self,pos):
        B8_pos=self.canvas.coords(self.B8.id)
        if pos[2] >= B8_pos[0] and pos[0] <= B8_pos[2]:
            if pos[3] >= B8_pos[1] and pos[3] <= B8_pos[3]:
                return True
        return False

    def golpea_B9(self,pos):
        B9_pos=self.canvas.coords(self.B9.id)
        if pos[2] >= B9_pos[0] and pos[0] <= B9_pos[2]:
            if pos[3] >= B9_pos[1] and pos[3] <= B9_pos[3]:
                return True
        return False
    


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=0.3

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B5(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B6(pos) == True:
            self.x=1
            self.y=0.5

        if self.golpea_B7(pos) == True:
            self.x=1
            self.y=1
            
        if self.golpea_B8(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B9(pos) == True:
            self.x=0.5
            self.y=1      
            

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1


class Bola11:                                #crea bola 11
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.B6= B6
        self.B7= B7
        self.B8= B8
        self.B9= B9
        self.B10= B10
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,560,210)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False

    def golpea_B6(self,pos):
        B6_pos=self.canvas.coords(self.B6.id)
        if pos[2] >= B6_pos[0] and pos[0] <= B6_pos[2]:
            if pos[3] >= B6_pos[1] and pos[3] <= B6_pos[3]:
                return True
        return False

    def golpea_B7(self,pos):
        B7_pos=self.canvas.coords(self.B7.id)
        if pos[2] >= B7_pos[0] and pos[0] <= B7_pos[2]:
            if pos[3] >= B7_pos[1] and pos[3] <= B7_pos[3]:
                return True
        return False

    def golpea_B8(self,pos):
        B8_pos=self.canvas.coords(self.B8.id)
        if pos[2] >= B8_pos[0] and pos[0] <= B8_pos[2]:
            if pos[3] >= B8_pos[1] and pos[3] <= B8_pos[3]:
                return True
        return False

    def golpea_B9(self,pos):
        B9_pos=self.canvas.coords(self.B9.id)
        if pos[2] >= B9_pos[0] and pos[0] <= B9_pos[2]:
            if pos[3] >= B9_pos[1] and pos[3] <= B9_pos[3]:
                return True
        return False


    def golpea_B10(self,pos):
        B10_pos=self.canvas.coords(self.B10.id)
        if pos[2] >= B10_pos[0] and pos[0] <= B10_pos[2]:
            if pos[3] >= B10_pos[1] and pos[3] <= B10_pos[3]:
                return True
        return False


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=-0.1

        if self.golpea_B5(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B6(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B7(pos) == True:
            self.x=1
            self.y=-0.2
            
        if self.golpea_B8(pos) == True:
            self.x=1
            self.y=0.1

        if self.golpea_B9(pos) == True:
            self.x=1
            self.y=1      

        if self.golpea_B10(pos) == True:
            self.x=1
            self.y=1       

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1


class Bola12:                                #crea bola 12
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.B6= B6
        self.B7= B7
        self.B8= B8
        self.B9= B9
        self.B10= B10
        self.B11= B11
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,560,230)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False

    def golpea_B6(self,pos):
        B6_pos=self.canvas.coords(self.B6.id)
        if pos[2] >= B6_pos[0] and pos[0] <= B6_pos[2]:
            if pos[3] >= B6_pos[1] and pos[3] <= B6_pos[3]:
                return True
        return False

    def golpea_B7(self,pos):
        B7_pos=self.canvas.coords(self.B7.id)
        if pos[2] >= B7_pos[0] and pos[0] <= B7_pos[2]:
            if pos[3] >= B7_pos[1] and pos[3] <= B7_pos[3]:
                return True
        return False

    def golpea_B8(self,pos):
        B8_pos=self.canvas.coords(self.B8.id)
        if pos[2] >= B8_pos[0] and pos[0] <= B8_pos[2]:
            if pos[3] >= B8_pos[1] and pos[3] <= B8_pos[3]:
                return True
        return False

    def golpea_B9(self,pos):
        B9_pos=self.canvas.coords(self.B9.id)
        if pos[2] >= B9_pos[0] and pos[0] <= B9_pos[2]:
            if pos[3] >= B9_pos[1] and pos[3] <= B9_pos[3]:
                return True
        return False


    def golpea_B10(self,pos):
        B10_pos=self.canvas.coords(self.B10.id)
        if pos[2] >= B10_pos[0] and pos[0] <= B10_pos[2]:
            if pos[3] >= B10_pos[1] and pos[3] <= B10_pos[3]:
                return True
        return False

    def golpea_B11(self,pos):
        B11_pos=self.canvas.coords(self.B11.id)
        if pos[2] >= B11_pos[0] and pos[0] <= B11_pos[2]:
            if pos[3] >= B11_pos[1] and pos[3] <= B11_pos[3]:
                return True
        return False


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B5(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B6(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B7(pos) == True:
            self.x=1
            self.y=0.2
            
        if self.golpea_B8(pos) == True:
            self.x=-0.1
            self.y=-0.1

        if self.golpea_B9(pos) == True:
            self.x=1
            self.y=1      

        if self.golpea_B10(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B11(pos) == True:
            self.x=1
            self.y=0.7     

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1


class Bola13:                                #crea bola 13
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.B6= B6
        self.B7= B7
        self.B8= B8
        self.B9= B9
        self.B10= B10
        self.B11= B11
        self.B12= B12
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,560,250)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False

    def golpea_B6(self,pos):
        B6_pos=self.canvas.coords(self.B6.id)
        if pos[2] >= B6_pos[0] and pos[0] <= B6_pos[2]:
            if pos[3] >= B6_pos[1] and pos[3] <= B6_pos[3]:
                return True
        return False

    def golpea_B7(self,pos):
        B7_pos=self.canvas.coords(self.B7.id)
        if pos[2] >= B7_pos[0] and pos[0] <= B7_pos[2]:
            if pos[3] >= B7_pos[1] and pos[3] <= B7_pos[3]:
                return True
        return False

    def golpea_B8(self,pos):
        B8_pos=self.canvas.coords(self.B8.id)
        if pos[2] >= B8_pos[0] and pos[0] <= B8_pos[2]:
            if pos[3] >= B8_pos[1] and pos[3] <= B8_pos[3]:
                return True
        return False

    def golpea_B9(self,pos):
        B9_pos=self.canvas.coords(self.B9.id)
        if pos[2] >= B9_pos[0] and pos[0] <= B9_pos[2]:
            if pos[3] >= B9_pos[1] and pos[3] <= B9_pos[3]:
                return True
        return False


    def golpea_B10(self,pos):
        B10_pos=self.canvas.coords(self.B10.id)
        if pos[2] >= B10_pos[0] and pos[0] <= B10_pos[2]:
            if pos[3] >= B10_pos[1] and pos[3] <= B10_pos[3]:
                return True
        return False

    def golpea_B11(self,pos):
        B11_pos=self.canvas.coords(self.B11.id)
        if pos[2] >= B11_pos[0] and pos[0] <= B11_pos[2]:
            if pos[3] >= B11_pos[1] and pos[3] <= B11_pos[3]:
                return True
        return False

    def golpea_B12(self,pos):
        B12_pos=self.canvas.coords(self.B12.id)
        if pos[2] >= B12_pos[0] and pos[0] <= B12_pos[2]:
            if pos[3] >= B12_pos[1] and pos[3] <= B12_pos[3]:
                return True
        return False


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B5(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B6(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B7(pos) == True:
            self.x=1
            self.y=1
            
        if self.golpea_B8(pos) == True:
            self.x=1
            self.y=0.3

        if self.golpea_B9(pos) == True:
            self.x=1
            self.y=-0.3      

        if self.golpea_B10(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B11(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B12(pos) == True:
            self.x=1
            self.y=0.7    

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1              

class Bola14:                                #crea bola 14
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,color):
        self.canvas= canvas
        self.pelota= pelota
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.B6= B6
        self.B7= B7
        self.B8= B8
        self.B9= B9
        self.B10= B10
        self.B11= B11
        self.B12= B12
        self.B13= B13
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,560,270)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False

    def golpea_B6(self,pos):
        B6_pos=self.canvas.coords(self.B6.id)
        if pos[2] >= B6_pos[0] and pos[0] <= B6_pos[2]:
            if pos[3] >= B6_pos[1] and pos[3] <= B6_pos[3]:
                return True
        return False

    def golpea_B7(self,pos):
        B7_pos=self.canvas.coords(self.B7.id)
        if pos[2] >= B7_pos[0] and pos[0] <= B7_pos[2]:
            if pos[3] >= B7_pos[1] and pos[3] <= B7_pos[3]:
                return True
        return False

    def golpea_B8(self,pos):
        B8_pos=self.canvas.coords(self.B8.id)
        if pos[2] >= B8_pos[0] and pos[0] <= B8_pos[2]:
            if pos[3] >= B8_pos[1] and pos[3] <= B8_pos[3]:
                return True
        return False

    def golpea_B9(self,pos):
        B9_pos=self.canvas.coords(self.B9.id)
        if pos[2] >= B9_pos[0] and pos[0] <= B9_pos[2]:
            if pos[3] >= B9_pos[1] and pos[3] <= B9_pos[3]:
                return True
        return False


    def golpea_B10(self,pos):
        B10_pos=self.canvas.coords(self.B10.id)
        if pos[2] >= B10_pos[0] and pos[0] <= B10_pos[2]:
            if pos[3] >= B10_pos[1] and pos[3] <= B10_pos[3]:
                return True
        return False

    def golpea_B11(self,pos):
        B11_pos=self.canvas.coords(self.B11.id)
        if pos[2] >= B11_pos[0] and pos[0] <= B11_pos[2]:
            if pos[3] >= B11_pos[1] and pos[3] <= B11_pos[3]:
                return True
        return False

    def golpea_B12(self,pos):
        B12_pos=self.canvas.coords(self.B12.id)
        if pos[2] >= B12_pos[0] and pos[0] <= B12_pos[2]:
            if pos[3] >= B12_pos[1] and pos[3] <= B12_pos[3]:
                return True
        return False
    
    def golpea_B13(self,pos):
        B13_pos=self.canvas.coords(self.B13.id)
        if pos[2] >= B13_pos[0] and pos[0] <= B13_pos[2]:
            if pos[3] >= B13_pos[1] and pos[3] <= B13_pos[3]:
                return True
        return False

    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B5(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B6(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B7(pos) == True:
            self.x=1
            self.y=1
            
        if self.golpea_B8(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B9(pos) == True:
            self.x=0.7
            self.y=0.3     

        if self.golpea_B10(pos) == True:
            self.x=0.7
            self.y=-0.3

        if self.golpea_B11(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B12(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B13(pos) == True:
            self.x=1
            self.y=0.7
            

        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1


class Bola15:                                #crea bola 15
    def __init__(self,canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,puntuacion,color):
        self.canvas= canvas
        self.pelota= pelota
        self.puntuacion=puntuacion
        self.B1= B1
        self.B2= B2
        self.B3= B3
        self.B4= B4
        self.B5= B5
        self.B6= B6
        self.B7= B7
        self.B8= B8
        self.B9= B9
        self.B10= B10
        self.B11= B11
        self.B12= B12
        self.B13= B13
        self.B14= B14
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,560,290)
        self.x=0   #cambia dir pelota
        self.y=0   #cambia dir pelota
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def golpea_pelota(self,pos):
        pelota_pos=self.canvas.coords(self.pelota.id)
        if pos[2] >= pelota_pos[0] and pos[0] <= pelota_pos[2]:
            if pos[3] >= pelota_pos[1] and pos[3] <= pelota_pos[3]:
                return True
        return False


    def golpea_B1(self,pos):
        B1_pos=self.canvas.coords(self.B1.id)
        if pos[2] >= B1_pos[0] and pos[0] <= B1_pos[2]:
            if pos[3] >= B1_pos[1] and pos[3] <= B1_pos[3]:
                return True
        return False

    def golpea_B2(self,pos):
        B2_pos=self.canvas.coords(self.B2.id)
        if pos[2] >= B2_pos[0] and pos[0] <= B2_pos[2]:
            if pos[3] >= B2_pos[1] and pos[3] <= B2_pos[3]:
                return True
        return False


    def golpea_B3(self,pos):
        B3_pos=self.canvas.coords(self.B3.id)
        if pos[2] >= B3_pos[0] and pos[0] <= B3_pos[2]:
            if pos[3] >= B3_pos[1] and pos[3] <= B3_pos[3]:
                return True
        return False


    def golpea_B4(self,pos):
        B4_pos=self.canvas.coords(self.B4.id)
        if pos[2] >= B4_pos[0] and pos[0] <= B4_pos[2]:
            if pos[3] >= B4_pos[1] and pos[3] <= B4_pos[3]:
                return True
        return False

    def golpea_B5(self,pos):
        B5_pos=self.canvas.coords(self.B5.id)
        if pos[2] >= B5_pos[0] and pos[0] <= B5_pos[2]:
            if pos[3] >= B5_pos[1] and pos[3] <= B5_pos[3]:
                return True
        return False

    def golpea_B6(self,pos):
        B6_pos=self.canvas.coords(self.B6.id)
        if pos[2] >= B6_pos[0] and pos[0] <= B6_pos[2]:
            if pos[3] >= B6_pos[1] and pos[3] <= B6_pos[3]:
                return True
        return False

    def golpea_B7(self,pos):
        B7_pos=self.canvas.coords(self.B7.id)
        if pos[2] >= B7_pos[0] and pos[0] <= B7_pos[2]:
            if pos[3] >= B7_pos[1] and pos[3] <= B7_pos[3]:
                return True
        return False

    def golpea_B8(self,pos):
        B8_pos=self.canvas.coords(self.B8.id)
        if pos[2] >= B8_pos[0] and pos[0] <= B8_pos[2]:
            if pos[3] >= B8_pos[1] and pos[3] <= B8_pos[3]:
                return True
        return False

    def golpea_B9(self,pos):
        B9_pos=self.canvas.coords(self.B9.id)
        if pos[2] >= B9_pos[0] and pos[0] <= B9_pos[2]:
            if pos[3] >= B9_pos[1] and pos[3] <= B9_pos[3]:
                return True
        return False


    def golpea_B10(self,pos):
        B10_pos=self.canvas.coords(self.B10.id)
        if pos[2] >= B10_pos[0] and pos[0] <= B10_pos[2]:
            if pos[3] >= B10_pos[1] and pos[3] <= B10_pos[3]:
                return True
        return False

    def golpea_B11(self,pos):
        B11_pos=self.canvas.coords(self.B11.id)
        if pos[2] >= B11_pos[0] and pos[0] <= B11_pos[2]:
            if pos[3] >= B11_pos[1] and pos[3] <= B11_pos[3]:
                return True
        return False

    def golpea_B12(self,pos):
        B12_pos=self.canvas.coords(self.B12.id)
        if pos[2] >= B12_pos[0] and pos[0] <= B12_pos[2]:
            if pos[3] >= B12_pos[1] and pos[3] <= B12_pos[3]:
                return True
        return False
    
    def golpea_B13(self,pos):
        B13_pos=self.canvas.coords(self.B13.id)
        if pos[2] >= B13_pos[0] and pos[0] <= B13_pos[2]:
            if pos[3] >= B13_pos[1] and pos[3] <= B13_pos[3]:
                return True
        return False

    def golpea_B14(self,pos):
        B14_pos=self.canvas.coords(self.B14.id)
        if pos[2] >= B14_pos[0] and pos[0] <= B14_pos[2]:
            if pos[3] >= B14_pos[1] and pos[3] <= B14_pos[3]:
                return True
        return False

    def remove(self):
        self.Destroy()
    

    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)  #cambia dir pelota
        pos= self.canvas.coords(self.id)

                
        if pos[1]<=140:                   # donde rebotan
            self.y=1                                     #rebote en y
        if pos[3]>= self.canvas_height-100: # donde rebotan
            self.y= -1

        if self.golpea_pelota(pos) == True:
            self.x=1
            self.y=1    

        if self.golpea_B1(pos) == True:
            self.x=1
            self.y=-1

        if self.golpea_B2(pos) == True:
            self.x=1
            self.y=0.8

        if self.golpea_B3(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B4(pos) == True:
            self.x=1
            self.y=-0.2

        if self.golpea_B5(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B6(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B7(pos) == True:
            self.x=1
            self.y=1
            
        if self.golpea_B8(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B9(pos) == True:
            self.x=0.3
            self.y=0.5      

        if self.golpea_B10(pos) == True:
            self.x=0.8
            self.y=0.4

        if self.golpea_B11(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B12(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B13(pos) == True:
            self.x=1
            self.y=1

        if self.golpea_B14(pos) == True:
            self.x=0.5
            self.y=0.7
                                               #todo bien
        if (pos[3]== self.canvas_height-100) and (pos[2]== self.canvas_width+90):
            self.puntuacion.tanto()
            
            
                                               #bien

        if (pos[1]==self.canvas_height-100)and (pos[3]== self.canvas_width+90):
            self.puntuacion.tanto()

    
        if (pos[2]== self.canvas_width-90)and (pos[3]==self.canvas_height-100):
            self.puntuacion.tanto()

        if (pos[0]==self.canvas_height+100)and (pos[2]==self.canvas_width+90):
            self.puntuacion.tanto()
       #

        if (pos[0]== self.canvas_height+100) and (pos[1]== self.canvas_width):
            self.puntuacion.tanto()

        if (pos[2]== self.canvas_height-100) and (pos[3]== self.canvas_width):
            self.puntuacion.tanto()    

             ###
            
               
        if pos[0]<=90:
            self.x=1
        if pos[2]>= self.canvas_width-90:
            self.x=-1             
            
            
            


class palo_billar: 
    def __init__(self,canvas,color):
        self.canvas= canvas
        global x1
        x1=20
        global y1
        y1=120
        global x2
        x2=250
        global y2
        y2=120
        self.id= canvas.create_line(x1,y1,x2,y2,fill=color,width=3)
        self.canvas.move(self.id,10,145)
        center = 100, 100
        self.x=0
        self.y=0
        self.canvas_width= self.canvas.winfo_width()
##        self.canvas_pointerxy= self.canvas.winfo_pointerxy()
        self.canvas_height = self.canvas.winfo_height()
##        self.canvas.bind_all('<Motion>',self.motion)
        self.canvas.bind_all('<space>',self.golpear)
        self.canvas.bind_all('<KeyPress-Left>',self.ir_izq)
        self.canvas.bind_all('<KeyPress-Right>',self.ir_der)
        self.canvas.bind_all('<KeyPress-Up>',self.ir_arriba)
        self.canvas.bind_all('<KeyPress-Down>',self.ir_abajo)
##        self.canvas.bind_all("<Button-1>", self.press)
##        self.canvas.bind_all("<B1-Motion>", self.motion)




##    def getangle(self,event):
##        dx = canvas.canvasx(event.x) - center[0]
##        dy = canvas.canvasy(event.y) - center[1]
##        try:
##            return complex(dx, dy) / abs(complex(dx, dy))
##        except ZeroDivisionError:
##            return 0.0 # cannot determine angle
##
##    def press(self,event):
##        # calculate angle at start point
##        global start
##        start = getangle(self,event)
##
##
##    def motion(self,event):
##        # calculate current angle relative to initial angle
##        global start
##        angle = getangle(self,event) / start
##        offset = complex(center[0], center[1])
##        newxy = []
##        for x, y in xy:
##            v = angle * (complex(x, y) - offset) + offset
##            newxy.append(v.real)
##            newxy.append(v.imag)
##        canvas.coords(self.id, *newxy)    

    



    def golpear(self,event):        
        self.canvas.move(self.id,self.x+35,self.y)
        
        


    def ir_izq(self,evt):
        self.canvas.move(self.id,self.x-35,self.y)


    def ir_arriba(self,evt):
        self.canvas.move(self.id,self.x,self.y-35)

    def ir_abajo(self,evt):
        self.canvas.move(self.id,self.x,self.y+35)    

        
        

        
##        x1+=20
##        y1+=120
##        x2+=250
##        y2+=120
        
                ##        quit(self.id)
##        canvas.create_line(x1,y1,x2,y2,fill=color,width=3)
##        self.canvas.move(self.id,self.x,self.y+35)


    def ir_der(self,evt):
        self.canvas.move(self.id,self.x+35,self.y)



    def quit(palo):
        palo.destroy() 


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)
        pos= self.canvas.coords(self.id)

        
        if pos[0]<=0:
            self.x=0
        elif pos[2]>= self.canvas_width:
            self.x=0

            

class palo_billar2: 
    def __init__(self,canvas,color):
        self.canvas= canvas
        global x1
        x1=20
        global y1
        y1=120
        global x2
        x2=250
        global y2
        y2=120
        self.id= canvas.create_line(x1,y1,x2,y2,fill=color,width=3)
        self.canvas.move(self.id,10,155)
        center = 100, 100
        self.x=0
        self.y=0
        self.canvas_width= self.canvas.winfo_width()
##        self.canvas_pointerxy= self.canvas.winfo_pointerxy()
        self.canvas_height = self.canvas.winfo_height()
##        self.canvas.bind_all('<Motion>',self.motion)
        self.canvas.bind_all('<space>',self.golpear)
        self.canvas.bind_all('<a>',self.ir_izq)
        self.canvas.bind_all('<d>',self.ir_der)
        self.canvas.bind_all('<w>',self.ir_arriba)
        self.canvas.bind_all('<s>',self.ir_abajo)
##        self.canvas.bind_all("<Button-1>", self.press)
##        self.canvas.bind_all("<B1-Motion>", self.motion)




##    def getangle(self,event):
##        dx = canvas.canvasx(event.x) - center[0]
##        dy = canvas.canvasy(event.y) - center[1]
##        try:
##            return complex(dx, dy) / abs(complex(dx, dy))
##        except ZeroDivisionError:
##            return 0.0 # cannot determine angle
##
##    def press(self,event):
##        # calculate angle at start point
##        global start
##        start = getangle(self,event)
##
##
##    def motion(self,event):
##        # calculate current angle relative to initial angle
##        global start
##        angle = getangle(self,event) / start
##        offset = complex(center[0], center[1])
##        newxy = []
##        for x, y in xy:
##            v = angle * (complex(x, y) - offset) + offset
##            newxy.append(v.real)
##            newxy.append(v.imag)
##        canvas.coords(self.id, *newxy)    

    



    def golpear(self,event):        
        self.canvas.move(self.id,self.x+35,self.y)
        
        


    def ir_izq(self,evt):
        self.canvas.move(self.id,self.x-35,self.y)


    def ir_arriba(self,evt):
        self.canvas.move(self.id,self.x,self.y-35)

    def ir_abajo(self,evt):
        self.canvas.move(self.id,self.x,self.y+35)    

        
        

        
##        x1+=20
##        y1+=120
##        x2+=250
##        y2+=120
        
                ##        quit(self.id)
##        canvas.create_line(x1,y1,x2,y2,fill=color,width=3)
##        self.canvas.move(self.id,self.x,self.y+35)


    def ir_der(self,evt):
        self.canvas.move(self.id,self.x+35,self.y)



    def quit(palo):
        palo.destroy() 


    def dibujar(self):
        self.canvas.move(self.id,self.x,self.y)
        pos= self.canvas.coords(self.id)

        
        if pos[0]<=0:
            self.x=0
        elif pos[2]>= self.canvas_width:
            self.x=0





### a square
##xy = [(50, 50), (150, 50), (150, 150), (50, 150)]
##
##polygon_item = c.create_polygon(xy)
##
##center = 100, 100
##
##def getangle(event):
##    dx = c.canvasx(event.x) - center[0]
##    dy = c.canvasy(event.y) - center[1]
##    try:
##        return complex(dx, dy) / abs(complex(dx, dy))
##    except ZeroDivisionError:
##        return 0.0 # cannot determine angle
##
##def press(event):
##    # calculate angle at start point
##    global start
##    start = getangle(event)
##
##def motion(event):
##    # calculate current angle relative to initial angle
##    global start
##    angle = getangle(event) / start
##    offset = complex(center[0], center[1])
##    newxy = []
##    for x, y in xy:
##        v = angle * (complex(x, y) - offset) + offset
##        newxy.append(v.real)
##        newxy.append(v.imag)
##    c.coords(polygon_item, *newxy)
##
##c.bind("<Button-1>", press)
##c.bind("<B1-Motion>", motion)


class Puntuacion:
    def __init__(self,canvas,color):
        self.puntuacion=0
        self.canvas=canvas
        self.id= canvas.create_text(200,25,font=("Barbieri-Book",34),text=self.puntuacion,fill=color)
        puntaje1= canvas.create_text(100,25,font=("Barbieri-Book",34),text="Puntos: ",fill='white')
        nombre= canvas.create_text(100,530,font=("Barbieri-Book",34),text="1 jugador ",fill='white')
        nombre2= canvas.create_text(700,530,font=("Barbieri-Book",34),text="2 jugador ",fill='white')

                
    def tanto(self):
        self.puntuacion+=1
        self.canvas.itemconfig(self.id,text=self.puntuacion)



          
##def funcion():
##
##    #import colision
##    import nombre1jugador
    
        

tk=Tk()
tk.title("billar")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=800,height=556,bd=0,highlightthickness=0)
imagen_fondo=PhotoImage(file="billar_julian2.png")  ##imagen fondo canvas
canvas.create_image(400,280,image=imagen_fondo)     ## cambiar pos img bg
canvas.pack()

tk.update()



puntuacion=Puntuacion(canvas,'white')
palo=palo_billar(canvas,'cyan')
palo2=palo_billar2(canvas,'orange')
pelota= Pelota(canvas,palo,palo2,puntuacion,'white')
B1=Bola1(canvas,pelota,'yellow2')
B2=Bola2(canvas,pelota,B1,'blue')
B3=Bola3(canvas,pelota,B1,B2,'red')
B4=Bola4(canvas,pelota,B1,B2,B3,'purple')
B5=Bola5(canvas,pelota,B1,B2,B3,B4,'orangered')
B6=Bola6(canvas,pelota,B1,B2,B3,B4,B5,'green')
B7=Bola7(canvas,pelota,B1,B2,B3,B4,B5,B6,'brown')
B8=Bola8(canvas,pelota,B1,B2,B3,B4,B5,B6,B7,'black')
B9=Bola9(canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,'yellow4')
B10=Bola10(canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,'blue2')
B11=Bola11(canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,'red2')
B12=Bola12(canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,'purple2')
B13=Bola13(canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,'darkorange')
B14=Bola14(canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,'green2')
B15=Bola15(canvas,pelota,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,puntuacion,'darkred')

##texto_fin_juego=canvas.create_text(250,200,font=("Barbieri-Book",34),text='Fin del Juego',\
##state='hidden')                                   
#bjugar = Button(tk, text = "Jugar", command = funcion).place(x=200, y=220)









##palo=palo_billar(canvas,'cyan')

while 1:
    pelota.dibujar()
    B1.dibujar()
    B2.dibujar()
    B3.dibujar()
    B4.dibujar()
    B5.dibujar()
    B6.dibujar()
    B7.dibujar()
    B8.dibujar()
    B9.dibujar()
    B10.dibujar()
    B11.dibujar()
    B12.dibujar()
    B13.dibujar()
    B14.dibujar()
    B15.dibujar()
    palo.dibujar()
    palo2.dibujar()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    

