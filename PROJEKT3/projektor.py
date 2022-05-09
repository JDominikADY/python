menu_options = {
    1: "Menünpont 1",
    2: "Mnenünpont 2",
    3: "Menünpont +",
    4: "Véga",
}

def print_menu():
    print(menu_options)
    for menupontIndex in menu_options:
        minta="{} --- {}"
        print(minta.format(menupontIndex,menu_options[menupontIndex]))
        #print(menu_options[menupontIndex])
    pass




while (True):
    print_menu()
    try:
        option = int(input("Válassz: "))
    except:
        option="nicsen ijen"
        pass

    if option==1:
        print("egy")
    elif option==2:
        print("kettő")
    elif option==3:
        print("három")
    elif option==4:
        print("négy")
    else:
        print("Te vadbarom debil gyerek állj le a szerekkel mert ezt nem tudom feldolgozni!")
