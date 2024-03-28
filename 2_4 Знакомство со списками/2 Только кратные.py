numbers = []
while True:
    number = int(input())
    if number == 0:
        break
    else:
        numbers.append(number)
print(list(filter(lambda number: number % len(numbers) == 0, numbers)))