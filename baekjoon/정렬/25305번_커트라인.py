import sys

x, y = map(int,sys.stdin.readline().split())

score_list = list(map(int, input().split()))

score_list = sorted(score_list)
score_list = score_list[::-1]

if len(score_list) == x:
    print(score_list[y-1])
