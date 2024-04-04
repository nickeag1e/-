for i in range(int(input())):
    string = input().lower()
    for j in range(1, len(string)):
        if string[j] < string[j - 1]:
            print((i, j))