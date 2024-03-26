numbers = set()
for i in range(int(input())):
    numbers = numbers | set(input())
print(len(numbers))