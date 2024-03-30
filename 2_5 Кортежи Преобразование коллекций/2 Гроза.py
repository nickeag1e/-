highs = [(int(input()), float(input())) for i in range(int(input()))]
for i in range(len(highs), -1, -1):
    for j in range(i, len(highs) - 1):
        if highs[j][0] < highs[j + 1][0]:
            highs[j], highs[j + 1] = highs[j + 1], highs[j]
        elif highs[j][0] == highs[j + 1][0] and highs[j][1] < highs[j + 1][1]:
            highs[j], highs[j + 1] = highs[j + 1], highs[j]
print(*highs, sep='\n')