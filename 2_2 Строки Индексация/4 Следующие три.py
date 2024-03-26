number = int(input()) - 1
print(''.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i % 26] for i in range(number, number + 4)))