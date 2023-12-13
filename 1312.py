
def count_numbers():
    liczby = {}
    while i := input("Podaj jakąś liczbę: "):
        try:
            i = int(i)
            if i not in liczby:
                liczby[i] = 1
            else:
                liczby[i] += 1
        except ValueError:
            print("Podana wartość nie jest liczbą!")

    for k in liczby:
        print(f'Liczba {k} wystąpiła {liczby[k]} razy.')


def count_letters_in_file(filein):
    letters = {}
    with open(filein, "r") as fin:
        for row in fin:
            for ch in row:
                if ch.isalpha():
                    if ch not in letters:
                        letters[ch] = 1
                    else:
                        letters[ch] += 1
    return letters


def count_numbers_in_file(infile):
    numbers = {}
    with open(infile, "r") as fin:
        for row in fin:
            row = row.split()
            for el in row:
                try:
                    el = int(el)
                    if el not in numbers:
                        numbers[el] = 1
                    else:
                        numbers[el] += 1
                except ValueError:
                    pass
    return numbers


def main():
    # print(count_letters_in_file('input.txt'))
    count_numbers()
    print(count_numbers_in_file('input.txt'))


if __name__ == "__main__":
    main()
