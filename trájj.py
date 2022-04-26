
szam=""

while szam=="":
    try:
        szam=int(input("Kérek egy számot: "))
    except:
        print("Ez nem szám volt")
    else:
        print("De hülye vagy?")
    finally:
        print("Megvagyunk!")

print(szam*2)


