from dzielniki import dzielniki
from sys import argv


def liczba_doskonala(n):
    return sum(dzielniki(n)) == n


def main():
    if len(argv) != 2:
        print(f"Usage {argv[0]} number")
        exit(1)
        
    print(liczba_doskonala(int(argv[1])))


if __name__ == "__main__":
    main()
