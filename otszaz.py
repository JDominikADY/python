def ertek(darab):
    if darab==1:
        return 500
    else:
        return darab*400+150

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

voltF=False
szam=0
for e in kosar:
    if e==arunev:
        if not voltF:
            szam=szam+1
            voltF=True
    if e=="F":
        voltF=False
print(str(szam) + " vásárlás során vettek belőle")


#6
print("6.feladat")
print(str(vasarlasDb) + "darab vételekor fizetendő: " + str(ertek(vasarlasDb)))

#7
print("7.feladat")
darabF=0
elozoIndex=0
keresettIndex=0

for i in range(0, len(kosar)):
    if kosar[i]=="F":
        darabF+=1
        elozoIndex=keresettIndex
        keresettIndex=i
        
    if darabF==sorszam:
        break

print(kosar[elozoIndex+1:keresettIndex])

if sorszam>1:
    darabKosar=kosar[elozoIndex+1:keresettIndex]
else:
    darabKosar=kosar[elozoIndex:keresettIndex]

stat={}
for e in darabKosar:
   if e in stat.keys():
       stat[e]+=1
   else:
       stat[e]=1

#print(stat)
for e in stat:
    print(str(stat[e]) + " " + e)

















