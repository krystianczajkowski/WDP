
def main():
    tabliczka()

def tabliczka():
    print('   1  2  3  4  5  6  7  8  9')
    for i in range(1, 10):
        print(i, end=' ')
        for j in range(1, 10):
            print(str(j*i).rjust(2),end=' ')
        print()


if __name__ == "__main__":
    main()
