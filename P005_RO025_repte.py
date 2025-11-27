# P005_RO025_repte.py


repte = int(input("repte de la materia sobre 100:"))
unitat = int(input("unitats sobre 10 punts:"))
tasca1 = int(input("resultat de la tasca1 sobre 10:"))
tasca2 = int(input("resultat de la tasca2 sobre 10:"))
tasca3 = int(input("resultat de la tasca3 sobre 10:"))

tasques = ((tasca1 + tasca2 + tasca3) / 3) *10

unitat = unitat *10
 
nota_final = (repte*70/100)+ (unitat *20/100) + (tasques *10/100)

print("nota final de la materia sobre 100 =", nota_final, repte)