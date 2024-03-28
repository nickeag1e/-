colors = [input() for i in range(int(input()))]
for i in range(int(input())):
    print(colors[i % len(colors)])