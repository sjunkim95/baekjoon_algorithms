import sys
input = sys.stdin.readline

N, M = map(int,input().split())

table_1 = [list(map(int, input().split())) for _ in range(N)]
table_2 = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        table_1[i][j] = table_1[i][j]+table_2[i][j]
        
for i in range(len(table_1)):
    print(*table_1[i])

