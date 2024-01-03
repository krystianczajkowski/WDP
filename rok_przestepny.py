from sys import argv

def main():
    print(rok_przestepny(int(argv[1])))

def rok_przestepny(rok):
    return True if rok % 4 == 0 or rok % 400 == 0 and not rok % 100 == 0 else False
        

if __name__ == "__main__":
    main()