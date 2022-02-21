import random

f=open("adatok.txt", "w")
be="hhe"
while be!="":
    be=input("Adide a számot: ")
    if be !="":
        f.write(be+"\n")

f.close()

f=open("adatok.txt", "r")
print(f.read())

f.close


f = open("adatok.txt", "a" )
for i in range(int(input("Mennyi random számot szeretnél?: "))):
    randa = str(random.randint(1, 100))
    f.write(randa+"\n")
    
f.close()

f=open("adatok.txt", "r")
print(f.read())
szamol = sum(1 for line in open('adatok.txt'))
f.close()

print(szamol)
