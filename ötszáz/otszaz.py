
f=open("penztar.txt")
kosar=[]
for sor in f:
    kosar.append(sor.strip())


f.close()
print("2.felad")
print("A fizetések száma: " + str(kosar.count("F")))


print("3.feladat")
print("Az első vásárló " + str(kosar.index("F"))+ " darab árucikket vásárolt.")




























