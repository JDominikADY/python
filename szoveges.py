v_igen = ["Igen", "I", "igen", "i"]
v_nem = ["Nem", "N", "nem", "n"]

print("""
-ÜDVÖZÖLLEK! KEZDJÜK A JÁTÉKOT!-

Az éjszaka közepén felébredsz. Száraz a torkod, szomjas vagy, ki mész inni? (Igen / Nem)
""")

v1 = input(">>")

if v1 in v_igen:
    print("\nKiérsz a konyhába, majd meghalassz valamiféle zörgést a spájzból. Bemész megnézni miaz? (Igen/ Nem)\n")

    v2 = input(">>")

    if v2 in v_igen:
        print("\nBelépsz a spájzba majd elfut elõtted egy egér, majd megáll a sarokban nem tud hová futni. A falnak van támasztva egy seprû. El kezded vele ütni az egeret? (Igen / Nem)\n")
        
        v3 = input(">>")

        if v3 in v_igen:
            print("\nEl kezded csapkodni az egeret, majd az egér felmászik a seprûre, végigfut a nyelén és belédharap. Másnap meghalsz a betegségbe amit hordozott.\n ---VÉGE A JÁTÉKNAK: VESZTETTÉL!---")

        elif v3 in v_nem:
            print("\nAz egér beszalad egy lyukba. Te pedig ideges vagy mert nem tudod hogy beleevett-e valamibe, mert lehet hogy fertõzött az egér. Kihívod a rágcsálóírtókat? (Igen / Nem)\n")

            v4 = input(">>")

            if v4 in v_igen:
                print("\nMásnap kijönnek a rágcsálóírtók, majd elmondod nekik a történteket és bevezeted õket a konyhába. Rövid vizsgálat után azt állapították meg hogy nagy az esély arra hogy az egér fertõzött volt és megfertõzte a csatornarendszert is. Megkérdezik hogy ittál-e a vízbõl. Te pedig azt mondod hogy nem, mert találtál egy üveg ásványvizet a nappaliban és azt ittad meg.\n A szakemberek azt kérik hogy menj ki a lakásból ugyanis több óra is lehet míg fertõtlenítik a helyszínt, és lehet hogy a vízszerelõket is ki kell hívni a vízvezetékek miatt. Kihívod a vízszerelõket? (Igen/Nem) \n")

                v5 = input(">>")

                if v5 in v_igen:
                    print("\nMíg csörgeted a vízszerelõket kiszalad egy ház az egérbõl és belédharap majd összeesel és sosem ébredsz fel\n---VÉGE A JÁTÉKNAK: VESZTETTÉL---\n")
                  
                if v5 in v_nem:
                    print("\n Úgy döntöttél nem hívod ki a vízeseket. Majd miután megbeszélted a teendõket a rágcsálóírtókkal elmész a boltba vízért mert elfogyott az ásványvízed.\n A boltban csak almalé van abból is már csak egy raklapnyi, mert már két hete nem érkezett ásványvíz szállítmány. Bevásárolsz 4l almalevet majd mikor kiérsz a boltból hívnak a rágcsálóírtók hogy nagy baj van mert megharapta õket az egér és kiderítették hogy gyilkos betegséget hordoz magában. Arra kérnek hogy azonnal menj haza hogy karanténba tudják zárni a házadat, de neked kell az ásványvíz mert az almalé is elfog fogyni ezután pedig nem lesz iható vized. Gondolkodsz hogy a másik városban van egy bolt, de az 50km-re van tõled. Elmész a boltba? (Igen/Nem)\n")

                    v6 = input(">>")

                    if v6 in v_igen:
                        print("\nElindultál az autóddal a messzi bolthoz, közben megszomjaztál és ittál az almalébõl. Az almalé fertõzött volt, nyomban rosszul lettél majd nekihajtottál egy fának bevágtad a fejet, de mire a mentõk kiértek már nem lehetett megmenteni. \n ---VÉGE A JÁTÉKNAK: VESZTETTÉL--- \n")

                    if v6 in v_nem:
                        print("\nGyorsan bepattansz az autóba mert úgy döntöttél nem mész el a másik boltba. Hamarosan hazaérsz ahol már az ajtóban várnak a szakemberek, látszik hogy rosszul vannak. Közelebb mész hozzájuk. Elmondják hogy a ház tele van fertõzött egerekkel és megállíthatatlannak tûnik a terjedése. Egyszercsak azt veszed észre hogy körbevesznek az egerek és rádugranak. Halálra marnak, harapnak. \n ---VÉGE A JÁTÉKNAK: VESZTETTÉL---\n \nA történtek után gyorsan terjed a vírus amit a falu neve alapján Somogyszobi-U-VIR21 - nek neveznek el. Pár éven belül elterjed az egész világon és az emberek 80% - a meghal.\n KÖSZÖNÖM A JÁTÉKOT!")
                    
            if v4 in v_nem:
                print("\n Nem hívtad ki a rágcsálóírtókat viszont csapvízet sem mertél inni. Szomjan haltál még az este.\n---VÉGE A JÁTÉKNAK: VESZTETTÉL---\n")
                
    elif v2 in v_nem:
        print("\nEgy egér jön elõ a csap mögül, de elfut mielõtt eltudnád dönteni hogy mit teszel vele. Lehet hogy a csatornarendszerbõl jött elõ az egér, KOCKÁZATOS inni belõle. Iszol a csapvízbõl? (Igen / Nem)\n")

        v3b = input(">>")

        if v3b in v_igen:
            print("\nEgy pohárba töltessz vizet majd megiszod, sokkal jobban érzed magad mert már kevésbé vagy szomjas. Aggaszt az az egér. Kihívod a rágcsálóírókat hogy körbenézzenek a házban.\n Másnap kijönnek majd felülvizsgálják a terepet és azt állapítják meg hogy lehetséges hogy az egér megfertõzte a vízet. Megkérdezik hogy ittál-e a vízbõl. Majd hirtelen összeesel és többé nem ébredsz fel. \n ---VÉGE A JÁTÉKNAK: VESZTETTÉL--- \n")

        elif v3b in v_nem:
            print("Összeesel a szomjúságtól, majd többé sosem ébredsz fel. \n ---VÉGE A JÁTÉKNAK: VESZTETTÉL---\n")
    else:
        print("\nNem értem a válaszodat. Viszlát!")

elif v1 in v_nem:
    print("\nAz éjszaka folyamán szomjan halsz, mert nem mentél ki inni.\n ---VÉGE A JÁTÉKNAK: VESZTETTÉL---\n")


else:
    print("\nNem értem a válaszodat. Viszlát")
