
f=open("ajto.txt")

kodok=[]
for egySor in f:
    kodok.append(egySor[:-1])


f.close
print(kodok)

#239451
print("2. feladat")
be=input("Adja meg, mi nyitja a zárat! ")


print("3. feladat")
sorszam=1
talalat=[]
for index,kod in enumerate(kodok,1):
    if kod==be:
        talalat.append(index)
    sorszam+=1

print("A nyitó kódszámok sorai: " + " ".join(str(szam) for szam in talalat))

print("4. feladat")
