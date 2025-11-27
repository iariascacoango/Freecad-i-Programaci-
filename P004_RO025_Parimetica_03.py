#P004_RO025_Parimetica_03.py
#ex 15 llibre de mates

a1 = -203
an = 902.5
d = 16.5

n = ((an - a1 ) / d ) + 1

print("n = ",n )
"""jdjfhdhhfh"""

k = n

n = 1
s = 0
print("n         a            s             \n")

while n < k+1:
    a = a1 + (n - 1) * d
    s= a + s
    print(n,"     " ,a, "     ",    s)
    n= n + 1