import sys
input = sys.stdin.readline
n = int(input())

table = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            table[i][j] = 1

cnt = 0

for i in range(len(table)):
    cnt += table[i].count(1)

print(cnt)
