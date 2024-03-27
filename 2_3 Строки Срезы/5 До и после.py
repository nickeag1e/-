find = 0
string = input()
for i in range(len(string)):
    if string[i] == '-':
        find = i
        break
print(string[find + 1:] + '-' + string[:find])