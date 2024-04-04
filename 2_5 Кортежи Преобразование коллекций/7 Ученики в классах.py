classes = [[] for i in range(11)]
for i in range(int(input())):
    for j in range(11):
        count = int(input())
        if count != 0:
            classes[j].append(count)
res = [sum(clas) / len(clas) if len(clas) != 0 else 0 for clas in classes]
print(res)
minc = maxc = 0
for i in range(len(res)):
    if res[i] > res[maxc]:
        maxc = i
    if res[i] < res[minc] and res[i] != 0:
        minc = i
print(minc + 1, maxc + 1)
