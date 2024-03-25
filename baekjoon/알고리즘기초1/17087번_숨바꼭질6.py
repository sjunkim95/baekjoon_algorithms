import sys
input = sys.stdin.readline

N, S = map(int,input().split())

def gcd(a, b):
    while b:
        a, b = b, a%b
        return a
    
dist_list = []

for _ in range(N):
    n = int(input())
    n = abs(n-S)
    dict_list.append(n)

