import sys 
N, M = map(int,sys.stdin.readline().split())
num_list = []
# num_list = list(range(1,N+1))
for i in range(1, N+1): 
    num_list.append(i)

for i in range(M):
    x, y = map(int,sys.stdin.readline().split())
    temp = num_list[x-1:y]
    temp = temp[::-1]
    num_list[x-1:y] = temp


print(*num_list)
        
    
        
