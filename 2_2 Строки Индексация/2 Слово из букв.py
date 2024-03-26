answer = ''
for i in range(int(input())):
    string = input()
    if i + 1 > len(string):
        answer = None
        break
    else:
        answer += string[-(i + 1)]
print(answer)