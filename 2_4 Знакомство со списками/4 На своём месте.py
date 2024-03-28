strings = [input() for i in range(int(input()))]
string = input()
number = -1
for i in range(len(strings) - 1):
    if strings[i] <= string < strings[i + 1]:
        number = i + 1
if number == -1:
    print(len(strings))
else:
    print(number)