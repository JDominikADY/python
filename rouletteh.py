import random
import datetime

#a számok
piros = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36)
fekete = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
zöld = 0
páros = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
páratlan= (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)

def fogadas():
    print("Piros = 1")
    print("Fekete = 2")
    print("zöld = 3")
    print("Páratlan = 4")
    print("páros = 5")
    print("-=-=-=-=-=-=-=-=-=-=-")
    játékos = int(input("Írd be a tippedet, 1-5: "))
    print("-=-=-=-=-=-=-=-=-=-=-")

    porget()
    nyv()

roulette = 1
while roulette > 0:

    startIdo=datetime.datetime.now()
    print(startIdo)
    
    def porget():
        porgetes = random.randint(1,36)
        print('Az eredmény: ',porgetes)
        print("-=-=-=-=-=-=-=-=-=-=-")

    def nyv():
        if (porget) == piros:
            print("$.45-t nyertél")
        elif (porget) == fekete:
            print("$.45-t nyertél")
        elif (porget) == zöld:
            print("$5.00-t nyertél")
        elif (porget) == páros:
            print("$.45-t nyertél")
        elif (porget) == páratlan:
            print("$.45-t nyertél")
        else:
            print("Vesztettél")
            print("-=-=-=-=-=-=-=-=-=-=-")
            print("-=-=-=-=-=-=-=-=-=-=-")
            print("-=-=-=-=-=-=-=-=-=-=-")

    fogadas()

