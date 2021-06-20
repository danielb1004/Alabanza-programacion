import random
# file = open("base_de_datos.txt")
drummers = ["Daniel","Alejandro","yeny","Samuel"]
number_drummers = random.randint(0, 3)

# confra = int(input("Hay culto de confraternidad?.. Si si 1, si no 0: "))
confra = 0
meetings = []
if confra == 0:
    meetings = ["Jueves","Domingo 8:00","Domingo 10:30","Domingo 12:30"]
elif confra == 1:
    meetings = ["Jueves","Domingo 8:00","Domingo 10:30","Domingo 5:00"]


salida = []
i = 0
while i < 4:
    number_drummers = random.randint(0, 3)
    drummer = drummers[number_drummers]
    if not(i == 2 and drummer == "Samuel"):
        if drummer in salida:
            pass
        else:
            salida.append(drummer)
            i += 1

    


print(salida)