import sys
input = sys.stdin.readline


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input())

print(factorial(num))
