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
