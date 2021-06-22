from os import close, truncate
import random

drummers = ["Daniel","Alejandro","Yeny","Samuel"]
number_drummers = random.randint(0, 3)



# confra = int(input("Hay culto de confraternidad?.. Si si 1, si no 0: "))
confra = 0
meetings = []
if confra == 0:
    meetings = ["Jueves","Domingo 8:00","Domingo 10:30","Domingo 12:30"]
elif confra == 1:
    meetings = ["Jueves","Domingo 8:00","Domingo 10:30","Domingo 5:00"]


def random1():
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

error = False
file = open("base_de_datos.txt",'r')
contents = file.read()
words = contents.split()

while True:
    salida = random1()
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
file = open("base_de_datos.txt",'a')
file.write("\n")
file.write(str(salida))
file.close()
print(words)
print(salida)