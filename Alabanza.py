from os import close, truncate
import random
import json

# confra = int(input("Hay culto de confraternidad?.. Si si 1, si no 0: "))
confra = 0
meetings = []
if confra == 0:
    meetings = ["Jueves","Domingo 8:00","Domingo 10:30","Domingo 12:30"]
elif confra == 1:
    meetings = ["Jueves","Domingo 8:00","Domingo 10:30","Domingo 5:00"]
def drummer():
    #   Esta funcion define un orden de bateristas random
    def random_orden():
        drummers = ["Daniel","Alejandro","Yeny","Samuel"]
        number_drummers = random.randint(0, 3)
        salida = []
        i = 0
        while i < 4:
            number_drummers = random.randint(0, 3)
            drummer = drummers[number_drummers]
            if not(i == 2 and drummer == "Samuel"):
                if not(drummer in salida):
                    salida.append(drummer)
                    i += 1
        return(salida)
    #   Esta funcion verifica que el orden no sea el mismo que la vez anterior
    def random_drummers():
        # file = open("base_de_datos.txt",'r')
        # contents = file.read()
        # words = contents.split()
        tf = open("base_de_datos.json", "r")
        words = json.load(tf)
        while True:
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
    return (drummers_outing)
drummers_out = drummer()


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
    slow_sons_mens_number = random.randint(1,27)
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

# union de arrays
sons = mens_out + womens_out + slow_mens_out + slow_womens_out

print(sons)

# print(slow_mens_out)
# print(mens_out)
# print(drummers_out)


