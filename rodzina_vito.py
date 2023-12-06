
domy = [1, 2, 4, 5, 7, 10]
def dystans_miedzy_punktami(pkt: list):
    odleglosci = {}
    for e in pkt:
        if e not in odleglosci:
            for f in pkt:
                if e - f != 0:
                    odleglosci.append(abs(e-f))
    return round(sum(odleglosci)/len(oldeglosci))
