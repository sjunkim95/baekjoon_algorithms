import sys
input = sys.stdin.readline

n = int(input())

count = 0

for i in range(n):
  for j in range(n):
    if i != j:
      count+=1

print(count)
