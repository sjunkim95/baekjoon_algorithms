n = int(input())
num_list = list(map(int,input().split()))

if len(num_list)==n:
    print(min(num_list), max(num_list))
