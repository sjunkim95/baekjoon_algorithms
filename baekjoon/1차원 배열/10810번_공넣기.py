import sys

m, n = map(int,sys.stdin.readline().split())
num_list = []
for i in range(1, m+1):
    num_list.append(0)

for a in range(n):
    i, j, k = (map(int,sys.stdin.readline().split()))
    for x in range(i-1, j):
        num_list[x] = k

print(*num_list)
    
