import random

def koszon(nev="kedves barátom"):
    koszonesek=("Jó napot kívánok","Szevasz","Csá","Heló","Szia")
    
    print(random.choice(koszonesek),nev)

koszonCount=0
def koszon2(nev="kedves barátom"):
    koszonesek=("Jó napot kívánok","Szevasz","Csá","Heló","Szia")
    
    print(koszonesek[koszonCount],nev)
    koszonCount=+1
    
koszon("Józsi")
koszon("Béla")
koszon("Juci")
koszon2()
koszon2("Sanyi")
