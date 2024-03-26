string = input()
print('\n'.join(string[i:i + 2] for i in range(0, len(string) - 1, 2)))
