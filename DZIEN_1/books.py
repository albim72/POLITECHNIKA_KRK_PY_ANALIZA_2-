class Book:
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def create_book(self):
        print("utworzono nowy obiekt klasy: Book")

    def print_book(self):
        print(f'książka: {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, typ oprawy: {self.oprawa}')

    def rabat(self,procent):
        return self.cena*procent/100



b1 = Book(45,"Wiedźmin","Andrzej Sapkowski")
b1.print_book()
print(f'rabat od ceny {b1.cena} zł wynosi: {b1.rabat(12)} zł')
