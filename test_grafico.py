from tkinter import *

from tkinter import messagebox
from tkinter.ttk import Combobox



window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="Jueves")
lbl.grid(column=0, row=0)

combo = Combobox(window)
combo['values']= ("Daniel", "Alejandro", "Samuel", "Yeny")
combo.current(1) #set the selected item
combo.grid(column=0, row=100)


lbl = Label(window, text="Domingo 8:00")
lbl.grid(column=0, row=200)
combo1 = Combobox(window)
combo1['values']= ("Daniel", "Alejandro", "Samuel", "Yeny")
combo1.current(1) #set the selected item
combo1.grid(column=0, row=300)


lbl = Label(window, text="Domingo 10:30")
lbl.grid(column=0, row=400)
combo2 = Combobox(window)
combo2['values']= ("Daniel", "Alejandro", "Samuel", "Yeny")
combo2.current(1) #set the selected item
combo2.grid(column=0, row=500)


lbl = Label(window, text="Domingo 12:30")
lbl.grid(column=0, row=600)
combo3 = Combobox(window)
combo3['values']= ("Daniel", "Alejandro", "Samuel", "Yeny")
combo3.current(1) #set the selected item
combo3.grid(column=0, row=700)


def clicked():
    print(combo3.get())
    messagebox.showinfo('Message title', 'Message content')

btn = Button(window,text='Click here', command=clicked)

btn.grid(column=100,row=100)

window.mainloop()