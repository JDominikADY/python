"""
f=open("proba.txt", "w")
f.write("Háló")
f.close()




def file_kiir(file_nev):
    f=open(file_nev)

    print(f.read())
    f.close



f=open("adatok.txt", "a")

be="hhe"
while be!="":
    be=input("Adide a szöveget: ")
    if be !="":
        f.write(be+"\n")

f.close()
file_kiir("adatok.txt")
"""

f=open("adatok.txt")
f2=open("adatokSorszam.txt", "w")

sorszam=1
for egySor in f:
    f2.write(str(sorszam)+" "+str(egySor))
    sorszam+=1



f2.close()
f.close()
