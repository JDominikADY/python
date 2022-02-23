
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
for kod in kodok:
    if kod==be:
        talalat.append(sorszam)
    sorszam+=1

print("A nyitó kódszámok sorai: " + " ".join(str(szam) for szam in talalat))


print("4. feladat")
dupla=[]
for index,kod in enumerate(kodok,1):
    for karakter in kod:
        if kod.count(karakter) > 1:
            dupla.append(index)

if len(dupla)>0:
    print(dupla[0])
else:
    print("Nem volt")
