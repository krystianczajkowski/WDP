def doskonale(n):
   return sum(dzielniki(n)) == n

def dzielniki(n):
    dziel = []
    for i in range(1, n):
        if not n % i:
            dziel.append(i)
    return dziel

def podzielniki(n):
    dziel = dzielniki(n)
    pierwsze = []
    if czy_pierwsza(n):
        pierwsze.append(n)
    for i in dziel:
        if czy_pierwsza(i):
            pierwsze.append(i)
    return pierwsze

def czy_pierwsza(n):
    if n == 1:
        return False
    d = [1]
    for i in range(2, n+1):
        if not n % i: 
            d.append(i)
    return len(d) == 2

def fibo(n, memo = {}):
    if (n < 2):
        return n
    if n not in memo:
        memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]

print(fibo(100))