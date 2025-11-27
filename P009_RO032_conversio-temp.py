# P009_RO032_conversio-temp.py

t= float(input("temperatura = "))
print("conversio a ºC = 1")
print ("conversio a ºF = 2")
conversio = int(input("prem 1 o 2 segons la conversio que vols = "))

if conversio == 1:
    tc = (5/9) * (t-32)
    print(t,"son",tc, "ºF")

if conversio ==2:
    tf= 32 + 9,t/5
# *t ??
    print(t,"son",tf, "ºC")