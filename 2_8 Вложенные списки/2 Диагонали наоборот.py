n = int(input())
matrix = [list(map(int, input().split(', '))) for i in range(n)]
for i in range(n):
    matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]
    print(*matrix[i])
print(sum([matrix[i][i] + matrix[i][n - i - 1] for i in range(n)]))