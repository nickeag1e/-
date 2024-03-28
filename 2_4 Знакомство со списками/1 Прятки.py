strings = [input() for i in range(int(input()))]
for j in range(int(input())):
    number = -1
    name = input()
    for k in range(len(strings)):
        if name in strings[k]:
            number = k + 1
            break
    print(number)