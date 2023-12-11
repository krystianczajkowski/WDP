
def liczba_doskonala(n):
   return sum(dzielniki(n)) == n


def dzielniki(n):
    dziel = []
    for i in range(1, (n//2)+1):
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
            if len(d) >= 2:
                return False
    return True


def fibo(n, memo = {}):
    if (n < 2):
        return n
    if n not in memo:
        memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]


def fibo_mniejsza_od_n(n):
    i = 0
    while fibo(i) < n:
        i += 1
    return fibo(i - 1)


def najwiekszy_wspolny_dzielnik(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def liczby_wzglednie_pierwsze(n):
    wzgl_pierwsze = []
    for i in range(1, n):
        if najwiekszy_wspolny_dzielnik(i, n) == 1:
            wzgl_pierwsze.append(i)
    return wzgl_pierwsze
