
def main():
    tabliczka()

def tabliczka_mnożenia():
    print('   1  2  3  4  5  6  7  8  9  10')
    for i in range(1, 11):
        print(i, end=' ')
        for j in range(1, 11):
            print(str(j*i).rjust(2),end=' ')
        print()

def tabliczka():
    wynik = '*'
    for i in range(1, 11):
        if len(str(i)) == 2:
            wynik += '\t ' + str(i)
        else:
            wynik += '\t  ' + str(i)

    print(wynik)
    for i in range(1, 11):
        print(i, end='\t')
        for j in range(1, 11):
            print(str(j*i).rjust(3), end='\t')
        print()

if __name__ == "__main__":
    main()
