N, X = map(int,input().split())
num_list = list(map(int,input().split()))

if len(num_list)==N:
    for i in range(len(num_list)):
        if num_list[i] < X:
            print(num_list[i])
