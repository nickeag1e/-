number = input()
print('\n'.join([number[i:-i] if i > 0 else number for i in range(len(number))]))