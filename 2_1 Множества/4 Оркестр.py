names = [set(), set(), set()]
for i in range(3):
    while True:
        name = input()
        if name == '':
            break
        else:
            names[i].add(name)
names = names[0] - names[1] - names[2] | names[1] - names[0] - names[2] | names[2] - names[0] - names[1]
print(*names, sep='\n')