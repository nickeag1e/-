rast = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        rast.append(n)
for i in range(len(rast), -1, -1):
    for j in range(i, len(rast) - 1):
        if rast[j] < rast[j + 1]:
            rast[j], rast[j + 1] = rast[j + 1], rast[j]
print(*rast, sep='->')