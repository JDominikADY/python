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


print("5. feladat")
aruIndex=kosar.index(arunev)
darabLista=kosar[:aruIndex]
print(darabLista)
vasarlasDb=darabLista.count("F")+ 1
print(vasarlasDb)
print("Az első vásárlás sorszáma" + str(vasarlasDb))




















