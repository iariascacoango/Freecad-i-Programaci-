#P004_RO25_Paritmetica_04.py

print(" Menú Progessió arimetica  ")
print(" ============================ \n") # \n serveix per fer espais al resultat
print(" Prem l'opcio de calcul  \n")
print("Opció 1: darrer terme an")
print("Opció 2: primer terme a1 ")
print("Opció 3: número de termes n")
print("Opció 4: diferéncia o raó d ")
opcio = int(input("Prem l'opció entre 1 i 4"))

if opcio == 1:
    a1 = eval(input("a1 = "))
    n = int(input("n = "))
    d = eval(input("d = " ))
    
    iteracions = n
    n= 1
    while n <= interacions:
        an = a1 + (n-1)* d
        
if opcio ==2:
    a
if opcio == 3:
    an = eval(input("an = "))
    a1 = eval(input("a1 = "))
    d = eval(input("d = "))
    
    n= ((a-a)/d) + 1
    
    if n== int(n):  # if n.is_integer
        print(" = ",int(n))
    else:
        print("El número de termes ha de ser un sencer")
    