# P008_RO38_for_n_imparells.py

from math import*

n = int(input("num d'imparells="))
suma = 0

for i in range(1,n+1):
    k = (2*i) -1
    suma = suma + k
print("suma =",suma)
if suma == pow(n,2):
    print("verdader")
else:
    print("fals")
