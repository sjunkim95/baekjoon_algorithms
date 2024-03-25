import sys
n = int(sys.stdin.readline())

num_list = [0]*10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1


for _ in range(1, len(num_list)):
    for i in range(len(num_list)):
        print(i)
