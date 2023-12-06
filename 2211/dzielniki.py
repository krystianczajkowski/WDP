
def dzielniki(n, is_inclusive=False):
    divs = []
    for i in range(1, (n//2)+1):
        if not n % i:
            divs.append(i)
    if is_inclusive:
        divs.append(n)
    return divs


def main():
    print(dzielniki(6, True))

if __name__ == "__main__":
    main()