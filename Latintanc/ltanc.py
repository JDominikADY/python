#1
f=open("tancrend.txt")
adatok=f.read().split("\n")[:-1]
f.close()
#print(adatok)

tancok=[]
for i in range(0,len(adatok),3):
    tancok.append(adatok[i:i+3])
#print(tancok)

    
#3
print("A sambát " + str(adatok.count("samba")) + " pár mutatta be")




        
