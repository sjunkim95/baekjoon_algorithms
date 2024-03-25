import sys
input = sys.stdin.readline

num_list = [int(input()) for i in range(28)]

for i in range(1,31):
    if i not in num_list:
        print(i)
