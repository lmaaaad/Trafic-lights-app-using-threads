from tkinter import *
import time
fenetre = Tk()
fenetre.title("TP2")
fenetre.configure(width=1000,height=300)

text1=Label(fenetre,fg='black')
text1.configure(font=('times',40,'bold'))
text1.place(x=20,y=20)

def show_time():
  localtime = time.localtime()
  result = time.strftime('%I:%M:%S %p',localtime)
  text1.config(text=result)

bouton1=Button(fenetre,text='tes',bg='red',fg='black',width=20,height=4,command=show_time)

bouton1.place(x=450,y=100)



fenetre.mainloop()