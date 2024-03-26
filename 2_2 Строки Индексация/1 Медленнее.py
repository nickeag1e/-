string = input()
print(''.join([string[i] * (i + 1) for i in range(len(string))]))