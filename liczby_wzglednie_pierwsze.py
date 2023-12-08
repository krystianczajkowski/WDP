

def liczby_wzglednie_pierwsze(a, b):
    if b < a:
        tmp = b 
        b = a
        a = tmp
        
    while b != 0:
        c = a % b
        a = b
        b = c
    return a == 1

print(liczby_wzglednie_pierwsze(33, 12))