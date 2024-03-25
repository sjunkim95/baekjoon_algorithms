import sys

m, n = map(int,sys.stdin.readline().split())
num_list = []
for i in range(1, m+1):
    num_list.append(i)

for i in range(n):
    i, j = (map(int,sys.stdin.readline().split()))
    temp = num_list[i-1]
    num_list[i-1]= num_list[j-1]
    num_list[j-1] = temp

print(*num_list)
    
