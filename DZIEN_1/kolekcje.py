print("Kolekcje języka Python")

liczby = [3,56,78,24,-45,1345,2.2,453,12,-56,0,789,0.33,1.2,456,-111,99,23]
print(liczby)
print(liczby[0])
#CTRL+D  - powielenie linii/bloku
#CTRL +/ - komentowanie/odkomentowanie linii/bloku
print(liczby[1])
print(liczby[2:7])
print(liczby[-1])
print(liczby[6:])
print(liczby[:8])

liczby.append(78)
print(liczby)

liczby.insert(4,101)
print(liczby)

liczby.remove(1345)
print(liczby)

del liczby[0]
print(liczby)

print(sorted(liczby,reverse=True))
print(liczby)

liczby.sort()
print(liczby)

nb = [4,4,4,4,4,1]

liczby = liczby + nb #konkatenacja list (połączenie)

print(liczby)
print(type(liczby))

#krotka (tuple)

miasta = ("Kraków","Lublin","Warszawa","Poznań","Wrocław","Kraków","Gdańsk")
print(miasta)
print(type(miasta))
print(miasta[2:5])
print(miasta.count("Kraków"))

#zbiór

kolory = {"zielony","niebieski","biały","czarny","czerwony","biały"}
print(kolory)
print(kolory)
print(kolory)

kolory.add("pomarańczowy")
print(kolory)
kolory.update(["fioletowy","magenta","szary"])
print(kolory)

liczby = list(set(liczby))
print(liczby)
