def doskonale(n):
   return sum(dzielniki(n)) == n

def dzielniki(n):
    dziel = []
    for i in range(1, n):
        if not n % i:
            dziel.append(i)
    return dziel

def podzielniki(n):
    dziel = dzielniki(n+1)

def czy_pierwsza(n):
    # if n < 2:
    #     return False
    for i in range(2, n+1):
        if n % i == 0:
           print(n, i, n % i) 

print(czy_pierwsza(1))
print(czy_pierwsza(2))
print(czy_pierwsza(3))
print(czy_pierwsza(4))
print(czy_pierwsza(5))