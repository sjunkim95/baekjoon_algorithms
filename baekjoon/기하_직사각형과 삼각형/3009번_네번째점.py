import sys
input = sys.stdin.readline

count = {}
table = [list(map(int, input().split())) for _ in range(3)]

for i in range(len(table)):
    for j in range(2):
        try: count[i][j] += 1
        except: count[i][j] = 1

print(count)
