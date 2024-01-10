from random import randint

def main():
    m = matrix(3, 3)
    for row in m:
        print(row)

    print(macierz_symetryczna(m))
    

def matrix(rows, cols):
    m = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(randint(0, 1))
        m.append(row)
    return m
    
def macierz_symetryczna(macierz):
    if len(macierz) != len(macierz[0]):
        return False
    for i in range(len(macierz)):
        for j in range(len(macierz)-1):
            if macierz[i][j] != macierz[j][i]:
                return False
    return True

        



        
        

        

main()
