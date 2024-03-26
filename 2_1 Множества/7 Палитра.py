colors = set()
colors_rep = set()
count_sum = 0
for i in range(int(input())):
    for j in range(int(input())):
        color = input()
        if color in colors or color in colors_rep:
            count_sum += 1
            colors_rep.add(color)
        else:
            colors.add(color)
print(len(colors_rep), len(colors_rep) + count_sum)