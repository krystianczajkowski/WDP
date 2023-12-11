
def count(str):
    """Count unique characters in a string."""
    counter = {}
    for e in str:
        if e not in counter:
            counter[e] = 1
        else:
            counter[e] += 1
    return counter


def isalpha_wdp(lttr):
    """Check if a character is a letter."""
    if len(lttr) != 1:
        return False
    return 64 < ord(lttr.upper()) < 91


def count_letters(str):
    """Count letters only in a string."""
    counter = {}
    for e in str:
        if isalpha_wdp(e):
            if e not in counter:
                counter[e] = 1
            else:
                counter[e] += 1
    return counter


def count_letters_case_insensitive(str):
    """Count letters in a string case-insensitve."""
    counter = {}
    for e in str:
        if isalpha_wdp(e):
            if e.lower() not in counter:
                counter[e] = 1
            else:
                counter[e] += 1
    return counter


def count_max_occurences(str, case_insensitive=False):
    """Count max occurences of a letter in a string.
    
    If the argument "case_insensitive" is not passed defaults to False
    and treats upper and lower letters as different.
    """
    if case_insensitive:
        counter = count_letters(str)
    else:
        counter = count_letters_case_insensitive(str)

    return (max(counter, key=lambda x: counter[x]), counter[max(counter, key=lambda x: counter[x])])
