from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from os import close, truncate
import random
import json
from os import remove
from os import path
from tkinter import scrolledtext

def main():
    
    window = Tk()

    window.title("Automatic generator for praise")

    window.geometry('900x500')

    lbl = Label(window, text="Jueves")
    lbl.grid(column=0, row=0)

    combo = Combobox(window)
    combo['values']= ("daniel", "alejandro", "samuel", "yeny")
    combo.current(1) #set the selected item
    combo.grid(column=0, row=100)


    lbl = Label(window, text="Domingo 8:00")
    lbl.grid(column=0, row=200)
    combo1 = Combobox(window)
    combo1['values']= ("daniel", "alejandro", "samuel", "yeny")
    combo1.current(1) #set the selected item
    combo1.grid(column=0, row=300)


    lbl = Label(window, text="Domingo 10:30")
    lbl.grid(column=0, row=400)
    combo2 = Combobox(window)
    combo2['values']= ("daniel", "alejandro", "samuel", "yeny")
    combo2.current(1) #set the selected item
    combo2.grid(column=0, row=500)


    lbl = Label(window, text="Domingo 12:30")
    lbl.grid(column=0, row=600)
    combo3 = Combobox(window)
    combo3['values']= ("daniel", "alejandro", "samuel", "yeny")
    combo3.current(1) #set the selected item
    combo3.grid(column=0, row=700)

    def drummer():
        #   Esta funcion define un orden de bateristas random
        def random_orden():
            drummers = ["daniel","alejandro","yeny","samuel"]
            number_drummers = random.randint(0, 3)
            salida = []
            i = 0
            while i < 4:
                number_drummers = random.randint(0, 3)
                drummer = drummers[number_drummers]
                if not(i == 2 and drummer == "samuel"):
                    if not(drummer in salida):
                        salida.append(drummer)
                        i += 1
            return(salida)
        #   Esta funcion verifica que el orden no sea el mismo que la vez anterior
        def random_drummers():
            while True:
                words = []
                words.append(combo.get())
                words.append(combo1.get())
                words.append(combo2.get())
                words.append(combo3.get())
                if words[0] == "alejandro" and words[1] == "alejandro" and words[2] == "alejandro":                    
                    messagebox.showinfo("ERROR","Por favor ponga los bateristas que tocaron")
                    break

                salida = random_orden()
                error = 0
                i = 0
                while i < 4:
                    if words[i] == salida[i]:
                        pass
                    else:
                        error += 1
                    i += 1
                if error == 4:
                    break    
            return(salida)
        
        drummers_outing = random_drummers()
        txt = scrolledtext.ScrolledText(window,width=30,height=10)
        txt.grid(column=1,row=900)
        txt.insert(INSERT,drummers_outing)
        return(drummers_outing)

    

        
    btn = Button(window,text='Generar orden de bateristas', command=drummer)

    btn.grid(column=200,row=100)

    # union de arrays
    def sons():
                # aqui definimos un numero random del las listas
        def new_sons_mens_number():
            new_sons_mens_number = random.randint(1, 37)
            new_sons_mens_number = str(new_sons_mens_number)
            return(new_sons_mens_number)

        def new_sons_womens_number():
            new_sons_womens_number = random.randint(1,23)
            new_sons_womens_number = str(new_sons_womens_number)
            return(new_sons_womens_number)

        def old_sons_mens_number():
            old_sons_mens_number = random.randint(1,16)
            old_sons_mens_number = str(old_sons_mens_number)
            return(old_sons_mens_number)

        def old_sons_womens_number():
            old_sons_womens_number = random.randint(1,2)
            old_sons_womens_number = str(old_sons_womens_number)
            return(old_sons_womens_number)

        def slow_sons_mens_number():
            slow_sons_mens_number = random.randint(1,26)
            slow_sons_mens_number = str(slow_sons_mens_number)
            return(slow_sons_mens_number)

        def slow_sons_womens_number():
            slow_sons_womens_number = random.randint(1,18)
            slow_sons_womens_number = str(slow_sons_womens_number)
            return(slow_sons_womens_number)

        # abriendo los json y guardando en diccionarios
        tfile = open("new_sons_mens.json", "r")
        new_sons_mens = json.load(tfile)

        tfile1 = open("new_sons_womens.json", "r")
        new_sons_womens = json.load(tfile1)

        tfile2 = open("old_sons_mens.json", "r")
        old_sons_mens = json.load(tfile2)

        tfile3 = open("old_sons_womens.json", "r")
        old_sons_womens = json.load(tfile3)

        tfile4 = open("slow_sons_mens.json", "r")
        slow_sons_mens = json.load(tfile4)

        tfile5 = open("slow_sons_womens.json", "r")
        slow_sons_womens = json.load(tfile5)

        # ciclos para escojer canciones
        # old_sons
        random_old = random.randint(1,5)
        random_old1 = random.randint(1,10)


        # mens
        mens_out = [] 
        mens_out.append(new_sons_mens[new_sons_mens_number()])
        if random_old == 1:
            mens_out.append(old_sons_mens[old_sons_mens_number()])
        else:
            mens_out.append(new_sons_mens[new_sons_mens_number()])
            while mens_out[0] == mens_out[1]:
                mens_out[1] = (new_sons_mens[new_sons_mens_number()])
        slow_mens_out = []
        slow_mens_out.append(slow_sons_mens[slow_sons_mens_number()])

        # Womens
        womens_out = []
        womens_out.append(new_sons_womens[new_sons_womens_number()])
        if random_old1 == 1:
            womens_out.append(old_sons_womens[old_sons_womens_number()])
        else:
            womens_out.append(new_sons_womens[new_sons_womens_number()])
            while womens_out[0] == womens_out[1]:
                womens_out[1] = (new_sons_womens[new_sons_womens_number()])
        slow_womens_out = []
        slow_womens_out.append(slow_sons_womens[slow_sons_womens_number()])
        sons = mens_out + womens_out + slow_mens_out + slow_womens_out

        txt = scrolledtext.ScrolledText(window,width=40,height=10)
        txt.grid(column=0,row=900)
        txt.insert(INSERT,sons)

        #messagebox.showinfo("El orden aleatorio de las canciones es",sons)
        #lbl2 = Label(window, text=str(sons))
        #lbl2.grid(column=0, row=900)
        return(sons)
    
    btn2 = Button(window,text='Canciones aleatorias', command=sons)
    btn2.grid(column=200,row=400)
   
   
    #lbl1 = Label(window, text="el orden de las canciones generado es")
    #lbl1.grid(column=0, row=800)


    window.mainloop()
    
if __name__ == '__main__':
    main()