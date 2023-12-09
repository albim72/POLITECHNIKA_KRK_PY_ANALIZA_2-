# przykład 1

n = 99

def hx(k):
    return k**3+1
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c + n + hx(b)
    return n

print(policz(3,7,8,2))
print(policz(1.11,87.3,-11.2,0.1))

print(n)

#przykład 2

def rank(*lang,nrrank,**inne):
    print(f"rankig języków programowania nr {nrrank}: pierwsze miejsca: {lang[0]}, "
          f"drugie miejsce: {lang[1]}, trzecie miejsce: {lang[2]}")

rank("Python","Java","C++",nrrank=56)
rank("Python","C#","Java","C++","JavaScript",nrrank=77,ver="5.5")

#funkcje anonimowe
print((lambda d:d+122)(10))
print((lambda d,f:(d+122)/f)(10,2))

b = lambda a,b,c=1:(a+b)/c

print(b(1,2,6))
print(b(1,2,))

def multi(n):
    return lambda a:a*n

print(multi(5)(9))

#zastosowania funkcji lambda
num = [5,7,13,0,-45,13,47,11,0,-345,57,0,-.5,6.,118,-562,899]

nbparz  = list(filter(lambda x:x%2==0,num))
print(nbparz)

cube = list(map(lambda x:x**3,num))
print(cube)

def dodaj(x):
    return x+9

dziewiec = list(map(dodaj,num))
print(dziewiec)

#zbuduj listę, która będzie się składała z wartości całkowitych z przedziału [1,100000],
#każda wartość to będzie wartość z przedziału podniesiona do potęgu drugiej
#list comprehension

kwadraty = [i**2 for i in range(1,1000000)]
print(kwadraty)

