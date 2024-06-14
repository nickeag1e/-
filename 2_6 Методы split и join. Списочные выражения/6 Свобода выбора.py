sep, n, string = input().split()
n = int(n)
print(sep[::-1].join([s for s in string.split(sep) if len(set(s)) >= n]))