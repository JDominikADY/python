class adatok:
    def __init__(self, sor1, sor2):
        vag=sor1.split(" ")
        self.ora=int(vag[0])
        self.perc=int(vag[1])
        self.telefonszam=vag[2]

        self.uzenet=sor2
        
    def idoperc(self):
        return self.ora*60+self.perc
