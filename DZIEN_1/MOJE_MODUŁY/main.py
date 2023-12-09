#import dane
#import dane as dn
from dane import ksiegarnia as filia
from dane import book as bk
from funkcje.bfunkcje import czytaj_liste,czytaj_slownik
from klasy.cklasa import CDane

print("_____________________ czytanie bezpośrednie _____________________")
print(filia)
print(bk)

print("_____________________ czytanie za pomocą funkcji _____________________")
czytaj_liste(filia)
czytaj_slownik(bk)

print("_____________________ czytanie za pomocą obiektu _____________________")
cd = CDane(filia,bk)
cd.czytajl()
cd.czytajs()
