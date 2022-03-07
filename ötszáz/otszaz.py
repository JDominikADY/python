
#1
f=open("penztar.txt")
kosar=[]
for sor in f:
    kosar.append(sor.strip())


f.close()

#2
print("2.feladta")
print("A fizetések száma: " + str(kosar.count("F")))


#3
print("3.feladat")
print("Az első vásárló " + str(kosar.index("F"))+ " darab árucikket vásárolt.")



#4
sorszam=int(input("Vásárlás sorszáma: "))
arunev=input("Árucikk neve: ")
darab=int(input("Darabszám: "))


#5
print("5. feladat")
aruIndex=kosar.index(arunev)
darabLista=kosar[:aruIndex]
print(darabLista)
vasarlasDb=darabLista.count("F")+ 1
print(vasarlasDb)
print("Az első vásárlás sorszáma" + str(vasarlasDb))

utolsoIndex=0
for i in range(0,len(kosar)):
    if kosar[i*-1-1]==arunev:
        utolsoIndex=len(kosar)-i
        break
darabLista=kosar[:utolsoIndex]
vasarlasDb=darabLista.count("F") + 1
print("Az utolsó vásárlás sorszáma:" +str(vasarlasDb))

voltF=False
szam=0
for e in kosar:
    if e==arunev:















