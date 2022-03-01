import math


def NRsuelo(n): #Calculo de la función suelo de la raiz cuadrada mediante el método de Newton
    x = n
    y = math.floor((x + 1) / 2)
    while y < x:
        x = y
        y = math.floor((x + n / x) / 2)
    return x

def trialdiv(n):
    L=[]
    m=NRsuelo(n)
    for i in range (2,m):
        while n%i==0 and n!=1:
            L.append(i)
            n=n/i
            m=NRsuelo(n)
    if n==1:
        return L
    else: 
        L.append(n)
        return L
