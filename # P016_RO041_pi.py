# P016_RO041_pi.py

n= int(input("numero de termes:"))

k=1
pi=0
i=1

while i< n+1:
    terme_n= i
    if terme_n % 2 !=0:
        pi= pi + (1/k)
    if terme_n % 2 ==0:
        pi= pi + (1/k) * (1)
print