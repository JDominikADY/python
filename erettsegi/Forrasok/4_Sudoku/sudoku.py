filenev=input("Adja meg a bemeneti fájl nevét: ")
sor=input("Adja meg egy sor számát: ")
oszlop=input("Adja meg az oszlop számát: ")


f=open(filenev)
sorok=f.read().split("\n")[:-1]
f.close()

print(sorok)
