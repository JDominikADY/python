#1
f=open("titanic.txt")
adatok=f.read().split("\n")

f.close()


#22
print("2. feladat: " + str(len(adatok)) + " db")


#333
print("3. feladat: " + str(sum(int(e.split(";")[1]) + int(e.split(";")[2]) for e in adatok)) + " fő")

ossz=0
for e in adatok:
    temp=e.split(";")
    tulelo=int(temp[1])
    eltunt=int(temp[2])
    ossz+=tulelo
    ossz+=eltunt
print("3. feladat: " + str(ossz) + " fő")


#4444
kulcsSzo=input("4. feladat: Kulcsszó: ")
van=False

#find()
for e in adatok:
    if e.find(kulcsSzo)>=0:
        van=True
        break

if van:
    print("Van találat!")
else:
    print("Nincs találat!")

adatok2=[]
for e in adatok:
    temp=e.split(";")
    temp[1]=int(temp[1])
    temp[2]=int(temp[2])
    adatok2.append(temp)
#print(adatok2)
    
talalat=[e for e in adatok2 if e[0].find(kulcsSzo)>-1]
#print(talalat)
if len(talalat)>0:
    print("Van találat!")
else:
    print("Nincs találat!")


#55555
print("5. feladat")
for e in talalat:
    print("\t" + e[0] + " " + str((e[1]+e[2]))+ " fő")
 #alt
print("\n".join(["\t" + e[0] + " " + str((e[1]+e[2]))+ " fő" for e in talalat]))


#666666
print("6. feladat")
arany=[]
for e in adatok2:
    if e[2]/(e[1]+e[2])>0.6:
        arany.append(e[0])

for e in arany:
    print("\t"+e)
    
print("6. feladat")
print("\r\n".join(["\t" + e[0] for e in adatok2 if e[2] / (sum(e[1:]))>0.6]))


#7777777
maximum=-1
maxkat=""
for e in adatok2:
    if e[1]>maximum:
        maximum=e[1]
        maxkat=e[0]
        
print("7. feladat" + maxkat)

print(max([e[1] for e in adatok2]))
print("7. feladat" + [k[0] for k in adatok2 if k[1] == max([e[1] for e in adatok2])])


