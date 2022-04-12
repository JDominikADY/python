#osztály definíció
class Kutya:
    #konstruktor
    def __init__(self,nev):
        self.nev=nev
    #osztály függvény
    def ugat(self):
        print("VAU-VAU")

#példányosítás
k=Kutya("Armageddon")
k.ugat()
print(k.nev)
#osztály változó értékadása
k.nev="Dezső"
print(k.nev)

#öröklés, leszármaztatás
class NemetJuhasz(Kutya):
    #új függvény
    def pitiz(self):
        print(self.nev + ": NEIN!")
    #függvény felülírás
    def ugat(self):
        print("WAU-WAU")

n=NemetJuhasz("Rex")
n.ugat()
n.pitiz()

n2=NemetJuhasz("Kondér")
n2.pitiz()
