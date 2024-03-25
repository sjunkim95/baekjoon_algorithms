import sys
input = sys.stdin.readline


n = int(input())
num_list = []

for i in range(2, n+1):
  if n % i == 0:
    while n % i == 0:
      n = n // i
      num_list.append(i)


for x in num_list:
  print(x)
