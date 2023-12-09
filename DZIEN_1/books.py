class Book:
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.dodatek = "brak"
        self.create_book()

    def create_book(self):
        print("utworzono nowy obiekt klasy: Book")

    def print_book(self):
        print(f'książka: {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, typ oprawy: {self.oprawa}')

    def rabat(self,procent):
        return self.cena*procent/100

    def getcena(self):
        return self.cena

    def setcena(self,nowacena):
        self.cena = nowacena

    @property
    def oprawa(self):
        return self._oprawa

    @property
    def dodatek(self):
        return self._dodatek

    @dodatek.setter
    def dodatek(self,nowydodatek):
        self._dodatek = nowydodatek
    @oprawa.setter
    def oprawa(self,nowaoprawa):
        self._oprawa = nowaoprawa
        if nowaoprawa == "twarda":
            self.dodatek = "obwoluta"



b1 = Book(45,"Wiedźmin","Andrzej Sapkowski")
b1.setcena(44)
b1.print_book()
print(f'rabat od ceny {b1.getcena()} zł wynosi: {b1.rabat(12)} zł')
print("druga wersja wydania: (zmiana oprawy)")
b1.oprawa = "twarda"
print(f"zmieniono oprawę książki na typ - {b1.oprawa} z dodatkiem: {b1.dodatek}")
b1.print_book()
