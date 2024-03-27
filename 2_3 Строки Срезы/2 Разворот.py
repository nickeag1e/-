string = input()
n = int(input())
m = int(input())
k = int(input())
k = -k if n > m else k
print(string[n:m:k])