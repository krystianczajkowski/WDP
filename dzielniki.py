
def dzielniki(n: int, is_inclusive=False) -> list:
    """Returns all divisors of a number in a list.
    
    If the argument 'is_inclusive' is not passed in, defaults to False,
    otherwise includes argument 'n' in the divisors.
    """
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