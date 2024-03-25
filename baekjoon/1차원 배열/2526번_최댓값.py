import sys 
#num_list = list(map(int,sys.stdin.readline().split()))


num_list = [int(input()) for i in range(9)]
for i in range(len(num_list)):
    if max(num_list)==num_list[i]:
        print(num_list[i])
        print(i+1)
