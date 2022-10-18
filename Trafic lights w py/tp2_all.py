
import time 
from tkinter import *
import threading 


color ='green'

def greenlight():
    global color
    rightc.itemconfig(green,fill="green")
    rightc.itemconfig(yellow,fill="white")
    rightc.itemconfig(red,fill="white")
    color = 'yellow' 
    
def yellowlight():
    global color
    rightc.itemconfig(green,fill="white")
    rightc.itemconfig(yellow,fill="yellow")
    rightc.itemconfig(red,fill="white")
    color='red'
def redlight():
    global color
    rightc.itemconfig(green,fill="white")
    rightc.itemconfig(yellow,fill="white")
    rightc.itemconfig(red,fill="red")
    color='green'


# Creation de la fentre 

fenetre=Tk()
fenetre.title("Timer")
fenetre.configure(width=700,height=500,bg='white')
title=Label(fenetre,text='Traffic lights',fg='yellow',bg='red')
title.config(font=('times',20,'bold'))

#left canvas
list_time=Listbox(fenetre,width=20,height=10)

list_time.insert(1,"1")
list_time.insert(1,"5")
list_time.insert(2,"25")
list_time.insert(3,"50")
list_time.insert(4,"100")
list_time.insert(5,"125")
list_time.insert(6,"150")
list_time.insert(7,"200")
list_time.insert(8,"250")
list_time.insert(9,"300")

list_time.select_set(0)

list_time.place(x=100,y=150)

#right canvas
rightc=Canvas(fenetre,width=345,height=660,bg='white')
rightc.place(x=350,y=35)
green=rightc.create_oval(110,100,170,160,width=3,fill='white')
rightc.create_rectangle(100,90,180,170,width=3)
yellow=rightc.create_oval(110,190,170,250,width=3,fill='white')
rightc.create_rectangle(100,180,180,260,width=3)
red=rightc.create_oval(110,280,170,340,width=3,fill='white')
rightc.create_rectangle(100,270,180,350,width=3)


def lance():
    greenlight()
    Timer = threading.Timer(1,tester)
    Timer.start()
    btn2.place_forget()

    btn1.place(x=200,y=100)


def tester():
    global color
    if color !='':
        if color=='green':
            greenlight()
        elif color=='yellow':
            yellowlight()
        elif color=='red' :
            redlight()
        timer = threading.Timer(int(list_time.get(ACTIVE)),tester)
        timer.start()
    else :
        color='green'

    
        
def quitter():
    global color
    color=''
    rightc.itemconfig(green,fill="white")
    rightc.itemconfig(yellow,fill="white")
    rightc.itemconfig(red,fill="white")
    print("Cancelling timer\n") 
    timer.cancel()

    
    


btn1=Button(rightc,text='TEST ',command=tester,fg='yellow',bg='red')
btn1.config(font=('times',16,'bold'))


btn2=Button(rightc,text='lance ',command=lance,fg='yellow',bg='red')
btn2.config(font=('times',16,'bold'))
btn2.place(x=200,y=100)


btn3=Button(rightc,text='QUITTER',command=quitter,fg='yellow',bg='red')
btn3.config(font=('times',16,'bold'))
btn3.place(x=200,y=180)

timer = threading.Timer(1,tester)

fenetre.mainloop()