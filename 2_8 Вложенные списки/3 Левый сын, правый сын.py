from math import log2
numbers = list(map(int, input().split()))
res = [numbers]
for i in range(1, int(log2(len(numbers)) + len(numbers) % 2) + 1):
    res.append([res[i - 1][j] + res[i - 1][j + 1] if j + 1 < len(res[i - 1]) else res[i - 1][j] + 0 for j in
                range(0, len(res[i - 1]), 2)])
if len(numbers) == 1:
    print(res[0][0])
else:
    for r in reversed(res):
        print(*r)