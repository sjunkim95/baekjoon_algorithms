import sys
input = sys.stdin.readline

def gcd(x, y):
    while y > 0:
        temp = y
        y = x % y
        x = temp
    return x

a, b = map(int,input().split())
c, d = map(int,input().split())

N = gcd(a*d + c*b, b*d)

print((a*d + c*b)//N,(b*d)//N)
