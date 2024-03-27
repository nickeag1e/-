string = input()
step = -int(input())
while len(string) > 0:
    if step < 0:
        print(string[step:])
        string = string[:step]
        step = -step
    else:
        print(string[:step])
        string = string[step:]
        step = -step