import sys
input = sys.stdin.readline

x, y = map(int,input().split())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(x)//((factorial(y))*(factorial(x-y))))
