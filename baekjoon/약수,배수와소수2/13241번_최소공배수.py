import sys

input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

x, y = map(int,input().split())
print(lcm(x, y))
