string = input()
while set('[]') & set(string):
    left = 0
    for i in range(len(string)):
        if string[i] == '[':
            left = i
        elif string[i] == ']':
            string = string[:left] + string[i + 1:]
            break
print(string)