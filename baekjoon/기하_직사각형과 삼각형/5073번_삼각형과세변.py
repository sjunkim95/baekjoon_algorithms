import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a + b <= c or a + c <= b or b + c <= a:  # 삼각형의 조건
        print("Invalid")
    elif a == b == c:  # 정삼각형의 조건
        print("Equilateral")
    elif a == b or b == c or c == a:  # 이등변삼각형의 조건
        print("Isosceles")
    else:  # 부등변삼각형의 조건
        print("Scalene")

'''
while True:
    a, b, c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    if (a+b) <= c or (a+c) <= b or (b+c) <= a:
        print("Invalid")
    elif a==b==c:
        print("Equilateral")
    elif (a==b) and (a+b) > c or (a==c) and (a+c) > b or (b==c) and (b+c) > a:
        print("Isosceles")
    elif (a+b) > c or (a+c) > b or (b+c) > a:
        print("Scalene")
'''
