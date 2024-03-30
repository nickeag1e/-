sweet_dreams = []
while True:
    dream = input().strip()
    if dream == 'разбитое корыто':
        break
    else:
        sweet_dreams.append(dream)

for i in range(len(sweet_dreams)):
    for j in range(len(sweet_dreams) - 2, i - 1, -1):
        if len(sweet_dreams[j]) > len(sweet_dreams[j + 1]):
            sweet_dreams[j], sweet_dreams[j + 1] = sweet_dreams[j + 1], sweet_dreams[j]

print(*sweet_dreams, sep='\n')
