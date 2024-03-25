import sys
input = sys.stdin.readline

length_list = list(map(int, input().split()))

length_list.sort()

if (length_list[0] + length_list[1]) > length_list[2]:
  print(sum(length_list))
if (length_list[0] + length_list[1]) <= length_list[2]:
  print((length_list[0]+length_list[1])*2-1)
