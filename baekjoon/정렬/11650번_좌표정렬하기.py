import sys
n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num_tuple = tuple(map(int,sys.stdin.readline().split()))
    num_list.append(num_tuple)

# 2번째원소 기준으로 오름차순, 숫자 같을경우 1번째 원소 기준으로 구분 
num_list.sort(key=lambda x:(x[1], x[0]))

for i in range(len(num_list)):
    print(*num_list[i])
