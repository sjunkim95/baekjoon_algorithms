import sys
input = sys.stdin.readline

n = int(input())
number = 1
if n == 1:
    print("1")

for i in range(1, n):
    number += (i*6)
    if n <= number:
        print(i+1)
        break
