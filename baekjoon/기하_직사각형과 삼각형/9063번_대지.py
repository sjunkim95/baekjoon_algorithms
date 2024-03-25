import sys
input = sys.stdin.readline

x_list = []
y_list = []
n = int(input())
if n < 2:
    print("0")
else:
    for _ in range(n):
        x, y = map(int,input().split())
        x_list.append(x)
        y_list.append(y)

    x_length = (max(x_list)-min(x_list))
    y_length = (max(y_list)-min(y_list))

    print(x_length*y_length)
