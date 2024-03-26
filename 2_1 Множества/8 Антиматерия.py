res = set()
repeat = set()
flag = True
while flag:
    sosud = set()
    while True:
        elem = input()
        if elem == '':
            flag = False
            break
        elif elem == '-1':
            break
        else:
            elem = int(elem)
            if elem in res and elem not in sosud:
                repeat.add(elem)
            else:
                sosud.add(elem)
    res = res | sosud
print(*res - repeat)
