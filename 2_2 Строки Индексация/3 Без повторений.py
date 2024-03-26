while True:
    string = input()
    if not string:
        break
    elif len(string) == len(set(string)):
        print(string)