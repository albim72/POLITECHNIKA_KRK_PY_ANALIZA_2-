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
