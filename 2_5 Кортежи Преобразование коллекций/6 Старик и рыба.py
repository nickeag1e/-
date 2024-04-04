fishes = []
while True:
    fish = input()
    if fish:
        fishes.append(fish)
    else:
        break
fishes_a = fishes + []
fishes_len = fishes_a + []
for i in range(len(fishes)):
    for j in range(len(fishes) - 1):
        if fishes_a[j].lower() > fishes_a[j + 1].lower():
            fishes_a[j], fishes_a[j + 1] = fishes_a[j + 1], fishes_a[j]
        if len(fishes_len[j]) > len(fishes_len[j + 1]):
            fishes_len[j], fishes_len[j + 1] = fishes_len[j + 1], fishes_len[j]

if fishes_a != fishes_len:
    for i in range(len(fishes)):
        if fishes_a[i] != fishes_len[i]:
            print(fishes_a[i], fishes_len[i])
            break
else:
    print('YES')
