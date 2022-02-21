import szoveges_jatek
import project_szamkitalalo
import snake2

menu_v = {
    1: "Szöveges kalandjáték",
    2: "Számkitaláló",
    3: "Az a kígyós játék",
    4: "Kilépés",
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def Szövegeskalandjáték():
     kalandjatek()

def option2():
     print('Handle option \'Option 2\'')

def kígyós():
     snake()

if __nev__=='__main__':
    while(True):
        print_menu()
        valasztas = ''
        try:
            valasztas = int(input('Enter your choice: '))
        except:
            print("Nem jó. Adj meg egy számot")
        if valasztas == 1:
           Szövegeskalandjáték()
        elif valasztas == 2:
            option2()
        elif valasztas == 3:
            kígyós()
        elif valasztas == 4:
            print("Köszi heló!")
        else:
            print("Nem értelek. Adj meg egy számot 1-4 között.")
