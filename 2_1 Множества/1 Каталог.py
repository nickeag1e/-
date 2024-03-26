names = set()
for i in range(int(input())):
    string = input()
    if string in names:
        print('ДА')
    else:
        print('НЕТ')
        names.add(string)