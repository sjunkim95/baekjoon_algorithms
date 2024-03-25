import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    table = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1:
                table[i][j] = j
                continue
            if i == j:
                table[i][j] = 1
            else:
                if j > i:
                    table[i][j] = table[i][j-1] + table[i-1][j-1]
    print(table[i][j])
