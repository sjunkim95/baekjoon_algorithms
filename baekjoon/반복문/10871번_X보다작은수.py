N, X = map(int,input().split())
num_list = list(map(int,input().split()))

if len(num_list)==N:
    for i in range(len(num_list)):
        if num_list[i] < X:
            print(num_list[i])
"""
# 이런 방법도 가
import sys

n,x = map(int, sys.stdin.readline().split())

for i in map(int, sys.stdin.readline().split()) :
    if i < x : print(i, end=" ")
"""
