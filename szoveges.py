v_igen = ["Igen", "I", "igen", "i"]
v_nem = ["Nem", "N", "nem", "n"]

print("""
-�DV�Z�LLEK! KEZDJ�K A J�T�KOT!-

Az �jszaka k�zep�n fel�bredsz. Sz�raz a torkod, szomjas vagy, ki m�sz inni? (Igen / Nem)
""")

v1 = input(">>")

if v1 in v_igen:
    print("\nKi�rsz a konyh�ba, majd meghalassz valamif�le z�rg�st a sp�jzb�l. Bem�sz megn�zni miaz? (Igen/ Nem)\n")

    v2 = input(">>")

    if v2 in v_igen:
        print("\nBel�psz a sp�jzba majd elfut el�tted egy eg�r, majd meg�ll a sarokban nem tud hov� futni. A falnak van t�masztva egy sepr�. El kezded vele �tni az egeret? (Igen / Nem)\n")
        
        v3 = input(">>")

        if v3 in v_igen:
            print("\nEl kezded csapkodni az egeret, majd az eg�r felm�szik a sepr�re, v�gigfut a nyel�n �s bel�dharap. M�snap meghalsz a betegs�gbe amit hordozott.\n ---V�GE A J�T�KNAK: VESZTETT�L!---")

        elif v3 in v_nem:
            print("\nAz eg�r beszalad egy lyukba. Te pedig ideges vagy mert nem tudod hogy beleevett-e valamibe, mert lehet hogy fert�z�tt az eg�r. Kih�vod a r�gcs�l��rt�kat? (Igen / Nem)\n")

            v4 = input(">>")

            if v4 in v_igen:
                print("\nM�snap kij�nnek a r�gcs�l��rt�k, majd elmondod nekik a t�rt�nteket �s bevezeted �ket a konyh�ba. R�vid vizsg�lat ut�n azt �llap�tott�k meg hogy nagy az es�ly arra hogy az eg�r fert�z�tt volt �s megfert�zte a csatornarendszert is. Megk�rdezik hogy itt�l-e a v�zb�l. Te pedig azt mondod hogy nem, mert tal�lt�l egy �veg �sv�nyvizet a nappaliban �s azt ittad meg.\n A szakemberek azt k�rik hogy menj ki a lak�sb�l ugyanis t�bb �ra is lehet m�g fert�tlen�tik a helysz�nt, �s lehet hogy a v�zszerel�ket is ki kell h�vni a v�zvezet�kek miatt. Kih�vod a v�zszerel�ket? (Igen/Nem) \n")

                v5 = input(">>")

                if v5 in v_igen:
                    print("\nM�g cs�rgeted a v�zszerel�ket kiszalad egy h�z az eg�rb�l �s bel�dharap majd �sszeesel �s sosem �bredsz fel\n---V�GE A J�T�KNAK: VESZTETT�L---\n")
                  
                if v5 in v_nem:
                    print("\n �gy d�nt�tt�l nem h�vod ki a v�zeseket. Majd miut�n megbesz�lted a teend�ket a r�gcs�l��rt�kkal elm�sz a boltba v�z�rt mert elfogyott az �sv�nyv�zed.\n A boltban csak almal� van abb�l is m�r csak egy raklapnyi, mert m�r k�t hete nem �rkezett �sv�nyv�z sz�ll�tm�ny. Bev�s�rolsz 4l almalevet majd mikor ki�rsz a boltb�l h�vnak a r�gcs�l��rt�k hogy nagy baj van mert megharapta �ket az eg�r �s kider�tett�k hogy gyilkos betegs�get hordoz mag�ban. Arra k�rnek hogy azonnal menj haza hogy karant�nba tudj�k z�rni a h�zadat, de neked kell az �sv�nyv�z mert az almal� is elfog fogyni ezut�n pedig nem lesz ihat� vized. Gondolkodsz hogy a m�sik v�rosban van egy bolt, de az 50km-re van t�led. Elm�sz a boltba? (Igen/Nem)\n")

                    v6 = input(">>")

                    if v6 in v_igen:
                        print("\nElindult�l az aut�ddal a messzi bolthoz, k�zben megszomjazt�l �s itt�l az almal�b�l. Az almal� fert�z�tt volt, nyomban rosszul lett�l majd nekihajtott�l egy f�nak bev�gtad a fejet, de mire a ment�k ki�rtek m�r nem lehetett megmenteni. \n ---V�GE A J�T�KNAK: VESZTETT�L--- \n")

                    if v6 in v_nem:
                        print("\nGyorsan bepattansz az aut�ba mert �gy d�nt�tt�l nem m�sz el a m�sik boltba. Hamarosan haza�rsz ahol m�r az ajt�ban v�rnak a szakemberek, l�tszik hogy rosszul vannak. K�zelebb m�sz hozz�juk. Elmondj�k hogy a h�z tele van fert�z�tt egerekkel �s meg�ll�thatatlannak t�nik a terjed�se. Egyszercsak azt veszed �szre hogy k�rbevesznek az egerek �s r�dugranak. Hal�lra marnak, harapnak. \n ---V�GE A J�T�KNAK: VESZTETT�L---\n \nA t�rt�ntek ut�n gyorsan terjed a v�rus amit a falu neve alapj�n Somogyszobi-U-VIR21 - nek neveznek el. P�r �ven bel�l elterjed az eg�sz vil�gon �s az emberek 80% - a meghal.\n K�SZ�N�M A J�T�KOT!")
                    
            if v4 in v_nem:
                print("\n Nem h�vtad ki a r�gcs�l��rt�kat viszont csapv�zet sem mert�l inni. Szomjan halt�l m�g az este.\n---V�GE A J�T�KNAK: VESZTETT�L---\n")
                
    elif v2 in v_nem:
        print("\nEgy eg�r j�n el� a csap m�g�l, de elfut miel�tt eltudn�d d�nteni hogy mit teszel vele. Lehet hogy a csatornarendszerb�l j�tt el� az eg�r, KOCK�ZATOS inni bel�le. Iszol a csapv�zb�l? (Igen / Nem)\n")

        v3b = input(">>")

        if v3b in v_igen:
            print("\nEgy poh�rba t�ltessz vizet majd megiszod, sokkal jobban �rzed magad mert m�r kev�sb� vagy szomjas. Aggaszt az az eg�r. Kih�vod a r�gcs�l��r�kat hogy k�rben�zzenek a h�zban.\n M�snap kij�nnek majd fel�lvizsg�lj�k a terepet �s azt �llap�tj�k meg hogy lehets�ges hogy az eg�r megfert�zte a v�zet. Megk�rdezik hogy itt�l-e a v�zb�l. Majd hirtelen �sszeesel �s t�bb� nem �bredsz fel. \n ---V�GE A J�T�KNAK: VESZTETT�L--- \n")

        elif v3b in v_nem:
            print("�sszeesel a szomj�s�gt�l, majd t�bb� sosem �bredsz fel. \n ---V�GE A J�T�KNAK: VESZTETT�L---\n")
    else:
        print("\nNem �rtem a v�laszodat. Viszl�t!")

elif v1 in v_nem:
    print("\nAz �jszaka folyam�n szomjan halsz, mert nem ment�l ki inni.\n ---V�GE A J�T�KNAK: VESZTETT�L---\n")


else:
    print("\nNem �rtem a v�laszodat. Viszl�t")
