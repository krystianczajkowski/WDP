
def choinka(wys):
    #   *
    #  ***
    # *****
    #   *
    for i in range(1, wys+1):
        print(' '*(wys-i), '*'*(i*2-1), sep='')

    if wys <= 5:
        for t in range(wys//2-1):
            print(" "*(wys-1), '*', sep='')
    else:
        for t in range(wys//2-1):
            print(" "*(wys-wys//4), '*'*(wys//4), sep='')
choinka(9)