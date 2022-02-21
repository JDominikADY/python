#Kérj be egy szót, amíg ez a nem üres addig rakd bele a szót a listába és kérj be egy szót


szo=input("Kérek egy szót: ")

lista=[]
lista.append(szo)
print(lista)

while szo != "":
    szo=input("Kérek egy szót: ")
    lista.append(szo)
    print(lista)

lista.reverse()
for item in lista:
  print(item)
print(lista)


for line in lista: 
    nagy = line.title() 
 
    print(nagy)
