import sys
input = sys.stdin.readline

n = int(input())

member_list = []

for i in range(n):
  age, name = input().split()
  member_list.append([int(age),name])

member_list.sort(key = lambda x:x[0])

for i in member_list:
  print(*i)

  
