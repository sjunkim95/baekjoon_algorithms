import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

if a == b == c and a+b+c == 180:
  print("Equilateral")
elif a + b + c == 180:
  if a == b:
    print("Isosceles")
  elif a == c:
    print("Isosceles")
  elif b == c:
    print("Isosceles")
  elif a != b != c:
    print("Scalene")
elif a + b + c != 180:
  print("Error")
