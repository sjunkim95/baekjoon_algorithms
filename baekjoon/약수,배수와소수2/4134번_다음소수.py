import sys
input = sys.stdin.readline

N = int(input().strip())


def prime(num):
    if num == 0:
        return 2
    elif num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return num

for _ in range(N):
    n = int(input().strip())
    while True:
        if n == prime(n):
            print(prime(n))
            break
        n += 1

    
