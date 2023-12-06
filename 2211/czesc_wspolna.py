
def czy_nalezy(e, lst):
    for ele in lst:
        if ele == e:
            return True
    return False

def czesc_wspolna(lst, lst1):
    wsp = []
    for e in lst:
        if czy_nalezy(e, lst1):
            wsp.append(e)
    return wsp

print(czesc_wspolna([1, 2, 3], [3, 4, 6]))
