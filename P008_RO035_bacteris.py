# P008_RO035_bacteris.py

nb = int(input("numero de bacteris="))
mb = int(input("maxim de bacteris="))
dia = 0

while nb <= mb:
    print("dia",dia,"nb=",nb)
    nb = nb*2
    dia = dia + 1
print("dia",dia,"nb=",nb)
