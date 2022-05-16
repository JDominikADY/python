#filenev=input("Adja meg a bemeneti fájl nevét: ")
#sor=input("Adja meg egy sor számát: ")
#oszlop=input("Adja meg az oszlop számát: ")
filenev="nehez.txt"
sor=1
oszlop=1

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

#print(adatok)
#print(adatok2)


tabla=adatok[:9]
lepesek=adatok[9:]
#print(tabla)
#print(lepesek)


print("3.feladat")
print("Az adott helyen szereplő szám: " + str(tabla[sor-1][oszlop-1]))
