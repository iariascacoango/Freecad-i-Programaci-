# P001_RO022_Area Triangle.py
# from math import* (importar tots els elements matematics)

from math import*
#a = 4 
a = int(input("valor d'a = "))

#b = 7
b = int(input("valor d'b = "))

#c = 6
c = int(input("valor d'c = "))


semiperimetre = (a + b + c)/2
t = semiperimetre
s = sqrt(t*(t-a)*(t-b)*(t-c))

print("t = ",t)
print("s = ", s)
#print( cos(s))
