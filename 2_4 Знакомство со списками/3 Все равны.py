strings = []
while True:
    string = input()
    if string:
        strings.append(string)
    else:
        break
l = len(max(strings, key=len))
for word in reversed(strings):
    if (l - len(word)) % 2 == 0:
        print('-' * ((l - len(word)) // 2) + word + '-' * ((l - len(word)) // 2))
    else:
        print('-' * ((l - len(word)) // 2) + word + '-' * ((l - len(word)) // 2 + 1))