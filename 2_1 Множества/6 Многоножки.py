set1 = set()
set2 = set()
set3 = set()
for i in range(int(input())):
    count = int(input())
    if count > 40:
        set1.add(count)
    if count % 2 == 0:
        set2.add(count)
    if count % 3 == 0:
        set3.add(count)
ans = set1 & set2 - set3 | set1 & set3 - set2 | set2 & set3 - set1
print(*ans)