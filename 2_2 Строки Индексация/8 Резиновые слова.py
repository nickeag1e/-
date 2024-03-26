string = input()
if len(string) % 2 == 0:
    for i in range(len(string) // 2 - 1, -1, -1):
        print(' ' * i + string[i] + ' ' * (len(string) // 2 - i - 1) * 2 + string[len(string) - i - 1])
else:
    print(' ' * (len(string) // 2) + string[len(string) // 2])
    for i in range(len(string) // 2 - 1, -1, -1):
        print(' ' * i + string[i] + ' ' * ((len(string) // 2 - i) * 2 - 1) + string[len(string) - i - 1])
