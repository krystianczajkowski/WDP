
def validate(password):
    num = False
    upper_case = False
    for ch in password:
        if ord(ch) in range(65, 91):
            upper_case = True
        if ord(ch) in range(48, 58):
            num = True
    return num and upper_case
