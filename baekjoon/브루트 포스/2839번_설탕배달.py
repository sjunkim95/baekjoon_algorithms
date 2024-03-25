import sys

input = sys.stdin.readline

n = int(input())
array = []

for i in range(n//3 + 1):
    for j in range(n//5 + 1):
        if n == ((i*3) + (j*5)):
            array.append((i+j))


if len(array) == 0:
    print('-1')
else:
    print(min(array))
