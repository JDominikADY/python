f=open("ajto.txt")

kodok=[]
for egySor in f:
    kodok.append(egySor[:-1])


f.close
print(kodok)
