import numpy as np

zr = np.zeros(17)
print(zr)
print(type(zr))

print("_"*50)

print(np.empty(8))

print("_"*50)

u = np.arange(1,77,3)
print(u)

m = np.array([6,6,6,6,6,34,24,6])
print(m)
print(type(m))

nb = [4,6,24,5,-3,52,6,78]
# nbx = [4,6,24,5,-3,52,6,78,11]
print(nb)
print(type(nb))

npnb = np.array(nb)
print(npnb)
print(type(npnb))

nl = nb + npnb
print(nl)
print(type(nl))
