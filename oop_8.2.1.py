class Auto():
    def __init__(self, marka, model, napidij):
        self.marka = marka
        self.model = model
        self.napidij = napidij
        self.szabad = True

    def kolcsonzes(self):
        if self.szabad == True:
            self.szabad = False
            print(f'A {self.marka} {self.model} most már ki van adva.')
        else:
            print(f'A {self.marka} {self.model} nincs bent.')

    def visszavetel(self, napok):
        if self.szabad:
            print(f'A {self.marka} {self.model} nincs kint.')
        else:
            self.szabad = True
            fizetendo = napok * self.napidij
            print(f'A {self.marka} {self.model} most már vissza van véve.A kölcsönzési díj {fizetendo} lesz.')



class Szemelyauto(Auto):
    def __init__(self, marka, model, napidij, szin):
        super().__init__(marka, model, napidij) #a super a felette levő ősosztály init metodusát hívja meg.Egy objektumot ad vissza
        self.szin = szin




class Lakoauto(Auto):
    def __init__(self, marka, model, napidij, ferohely):
        super().__init__(marka, model, napidij)
        self.ferohely = ferohely


class Teherauto(Auto):
    def __init__(self, marka, model, napidij, teherbiras):
        super().__init__(marka, model, napidij)
        self.teherbiras = teherbiras

def main():
    jarmuvek = [
        Szemelyauto("opel", "astra", 5000, "piros"),
        Lakoauto("iveco", "bvb", 10000, 4),
        Teherauto("ford", "transit", 8000, 3.5),
        Szemelyauto("fiat","tipo",4000,"fehér")
    ]

    while True:
        print("\n Autókölcsönző")
        print("1.Listázás")
        print("2.Bérlés")
        print("3.Visszavétel")
        print("4.Kilépés")

        valasztas = input("Válasszon egy és négy között: ")

        if valasztas == "1":
            print("Autólista")
            for i, jarmu in enumerate(jarmuvek):
                if jarmu.szabad:
                    allapot = "Bérelhető"
                else:
                    allapot = "Kiadva"

                allapot = "Bérelhető" if jarmu.szabad else "Kiadva"
               # allapot = "Bérelhető" if jarmu.szabad else "Kiadva"  #ez a sor a for ciklust és a benne lévő feltételeket kiváltja

                print(f'{i + 1}. {jarmu.marka} {jarmu.model} {jarmu.napidij} ft/ nap {allapot}')
        elif valasztas == "2":
            print("Bérlés")
            sorszam = int(input("Kérem a bérelendő autó sorszámát: "))
            if 1 <= sorszam <= len(jarmuvek):
                jarmuvek[sorszam - 1].kolcsonzes()
            else:
                print("Nincs ilyen sorszámú jármű.")
        elif valasztas == "3":
            print("Visszavétel")
            sorszam = int(input("Kérem a visszahozott autó sorszámát: "))
            if 1 <= sorszam <= len(jarmuvek):
                napok = int(input("Kérem a bérelt napok számát: "))
                jarmuvek[sorszam - 1].visszavetel(napok)
            else:
                print("Nincs ilyen sorszámú jármű.")
        elif valasztas == "4":
            print("4")
            break
        else:
            print("Érvénytelen választás, próbálja újra.")



    """print(jarmu_1.marka)
    jarmu_1.kolcsonzes()
    jarmu_2.kolcsonzes()
    jarmu_1.visszavetel(4)
    jarmu_3.kolcsonzes()
    jarmu_1.kolcsonzes()
    jarmu_2.visszavetel(8)"""

if __name__ == "__main__":
    main()


