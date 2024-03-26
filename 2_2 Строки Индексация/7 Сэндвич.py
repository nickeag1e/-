string = input()
j = len(string) // 2 - 1 if len(string) % 2 == 0 else len(string) // 2
for i in range(j):
    print(string[i] + string[j + i + 1], end='')
if len(string) % 2:
    print(string[j])
else:
    print(string[j] + string[-1], end='')
