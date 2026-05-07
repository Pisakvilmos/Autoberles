class Auto:
    def __init__(self, marka, model, napidij):
        self.marka = marka
        self.model = model
        self.napidij = napidij
        self.szabad = True

    def kolcsonzes(self):
        if self.szabad:
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
            print(f'A {self.marka} {self.model} most már bent van. Fizetendő: {fizetendo} forint')


class Szemelyauto(Auto):
    def __init__(self, marka, model, napidij, szin):
        super().__init__(marka, model, napidij)
        self.szin = szin



class Lakoauto(Auto):
    def __init__(self, marka, model, napidij, ferohely):
        super().__init__(marka, model, napidij)
        self.ferohely = ferohely



class Teherauto(Auto):
    def __init__(self, marka, model, napidij, teherbiras):
        super().__init__(marka, model, napidij)
        self.teherbiras = teherbiras


jarmu_1 = Szemelyauto("opel", "astra", 5000, "piros")
jarmu_2 = Lakoauto("iveco", "bvb", 10000, 4)
jarmu_3 = Teherauto("ford", "transit", 8000, 3.5)

print(jarmu_1.marka)
jarmu_1.kolcsonzes()
jarmu_2.kolcsonzes()
jarmu_1.visszavetel(5)
jarmu_1.kolcsonzes()
jarmu_2.visszavetel(8)