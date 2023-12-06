from dzielniki import dzielniki
from sys import argv

def liczba_doskonala(n):
    return sum(dzielniki(n)) == n

def main():
    print(liczba_doskonala(int(argv[1])))


if __name__ == "__main__":
    main()