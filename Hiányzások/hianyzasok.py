
#masodikverzio
#elsoverzio
f=open("naplo.txt")
adatok=f.read().split("\n")
f.close()

#1 FELADAT
naplo=[]
honap=0
nap=0
for e in adatok:
    if e[0]=="#":
        # 01 15
        honap=int(e[2:3])
        nap=int(e[5:])
        #print(honap)
    else:
        temp=[]
        temp.append(honap)
        temp.append(nap)
        #nev + hianyzas berakasa
        vag=e.split(" ")
        temp.append(" ".join(vag[0:2]))
        temp.append(vag[2])
        naplo.append(temp)

#print(naplo)


#2 FELADAT
print("2.feladat\nA naplóban " + str(len(naplo)) + " hiányzás van.")


#3 FELADAT
igazolt=0
igazolatlan=0
for e in naplo:
    igazolt+=e[3].count("X")
    igazolatlan+=e[3].count("I")

print("3.feladat\nAz igazolt hiányzások száma " + str(igazolt) + ", az igazolatlanoké " + str(igazolatlan) + ".")


#4 FELADAT
def hetnapja(honap,nap):
    napnev = ("vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat")
    napszam = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap-1]+ nap) % 7
    return napnev[napsorszam]


#5 FELADAT
print("5. feladat")
honap=int(input("A hónap sorszáma= "))
nap=int(input("a nap sorszáma= "))
print("Azon a napon " + hetnapja(honap,nap) + " volt.")


#6 FELADAT
print("6.feladat")
napnev=input("A nap neve: ")
ora=int(input("Az óra száma: "))

db=0
for e in naplo:
    if hetnapja(e[0],e[1])==napnev:
        if e[3][ora-1]=="X" or e[3][ora-1]=="I":
            db+=1

print("Ekkor összesen " + str(db) + " óra hiányzás történt.")

db=sum([e[3][ora-1] in ["X","I"] for e in naplo if hetnapja(e[0],e[1])==napnev])
#print(db)


#7 FELADAT
stat={}
for e in naplo:
    if e[2] in stat.keys():
        stat[e[2]] += e[3].count("X")+e[3].count("I")
    else:
        stat[e[2]] = e[3].count("X")+e[3].count("I")

maximum=0
for e in stat:
    if stat[e]>maximum:
        maximum=stat[e]

print("A legtöbbet hiányzó tanulók: ", end="")
for e in stat:
    if stat[e]==maximum:
        print(e,end=" ")

print()
maximum=max(stat.values())
leg=[e for e in stat if stat[e]==maximum]

print(leg)
print("A legtöbbet hiányzó tanulók: " + " ".join(leg))

#print(stat)
#print(maxi(stat))






















