import sys

input = sys.stdin.readline

N, M = map(int,input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
ans1_list = []
ans2_list = []

ans1_list = list(set(A_list).difference(B_list))
ans2_list = list(set(B_list).difference(A_list))

print(len(ans1_list) + len(ans2_list))
