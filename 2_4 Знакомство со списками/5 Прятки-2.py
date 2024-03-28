strings = [input() for i in range(int(input()))]
names = [input() for j in range(int(input()))]
for string in strings:
    if len(set(string.replace('.', '').split()) & set(names)) == len(names):
        print(string)