
def dystans_miedzy_punktami(pkt: list):
    """Calculate sum of distances for each point."""
    odleglosci = {}
    for i, e in enumerate(pkt):
        tmp_pkt = pkt[:i] + pkt[i+1:]
        for f in tmp_pkt:
            if e not in odleglosci:
                odleglosci[e] = abs(e-f)
            else:
                odleglosci[e] += abs(e-f)
    return get_min_value(odleglosci)


def get_min_value(dict):
    """Returns smallest value from a dict.
    
    If two keys have the same value return only the first one.
    """
    min_v, min_k = 2e32, None
    for key in dict:
        value = dict[key]
        if value < min_v:
            min_v, min_k = value, key
            
    return min_k, min_v


def main():
    domy = [1, 2, 4, 5, 7, 10]
    domy_ = domy[::-1]
    print(dystans_miedzy_punktami(domy))
    print(dystans_miedzy_punktami(domy_))


if __name__ == "__main__":
    main()
