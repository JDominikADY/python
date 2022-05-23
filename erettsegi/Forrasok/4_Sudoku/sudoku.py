import math

def oszlop_ban_van_e(oszlop,ertek):
    for o in tabla:
        if o[oszlop]==ertek:
            return True
        return False

def resztabla(sor,oszlop):
    s=math.ceil((sor+1)/3)-1
    o=math.ceil((oszlop+1)/3)

    return s*3+o
    
    
        
#filenev=input("Adja meg a bemeneti fájl nevét!")
#sor=int(input("Adja meg egy sor számát!"))
#oszlop=int(input("Adja meg egy oszlop számát!"))
filenev="nehez.txt"
sor=7
oszlop=7

f=open(filenev)
sorok=f.read().split("\n")[:-1]
f.close()


adatok=[]
for sor in sorok:
    adatok.append(sor.split(" "))

adatok2=[]
for sor in adatok:
    temp=[]
    for elem in sor:
        temp.append(int(elem))
    adatok2.append(temp)
    
print(adatok)
print(adatok2)

tabla=adatok[:9]
lepesek=adatok[9:]

print("3. feladat")

#print("Az adott helyen szereplő szám: "+ str(tabla[sor-1][oszlop-1]))

if tabla[sor-1][oszlop-1]==0:
    print("Adott helyet még nem töltötték ki.")
else:
    print("Az adott helyen szereplő szám: "+str(tabla[sor-1][oszlop-1]))


s=math.ceil(sor/3)-1
o=math.ceil(oszlop/3)



print("A hely a(z) {} résztáblázathoz tartozik.".format(s*3+o))

db=0
for s in tabla:
    db+=s.count("0")
print("4. feladat")
print("Az üres helyek aránya: {:.0%}".format(db/81))


print("5. feladat")
for lepes in lepesek:
    t_s=int(lepes[1])-1 #sor
    t_o=int(lepes[2])-1 #oszlop

    print(resztabla(t_s,t_o))

    volt=False
    for i in range(0,9):
        for k in range(0,9):
            if resztabla(t_s,t_o)==resztabla(i,k):
                if tabla[i][k]==lepes[0]:
                    volt=True
                    
    
    print(lepes)
    print(tabla[int(lepes[1])-1][int(lepes[2])-1])

    print(lepes[0] in tabla[int(lepes[1])-1])
    
    if tabla[t_s][t_o]!="0":
        print("A helyet már kitöltötték.")
    elif lepes[0] in tabla[t_s]:
        print("Az adott sorban már szerepel a szám.")
    elif oszlop_ban_van_e(t_o,lepes[0]):
        print("Az adott oszlopban már szerepel a szám.")
    elif volt:
        print("Az adott résztáblázatban szerepel a szám")
    else:
        print("A lépés megtehető")
        














    
