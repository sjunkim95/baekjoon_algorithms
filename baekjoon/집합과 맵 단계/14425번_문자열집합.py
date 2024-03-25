import sys
from itertools import count

input = sys.stdin.readline

N, M = map(int,sys.stdin.readline().split())
count = 0
string_dict = {}

for i in range(N):
    data = str(input().strip())
    string_dict[data] = True

for i in range(M):
    test_string = str(input().strip())
    if test_string in string_dict:
        count += 1

print(count)
