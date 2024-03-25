import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
a = int(input())

array = []


for _ in range(1, N):
    num = int(input())
    array.append(num-a)
    a = num

g = array[0]

for i in range(1, len(array)):
    g = gcd(g, array[i])
    
result = 0

for i in array:
    result += i // g -1
print(result)
