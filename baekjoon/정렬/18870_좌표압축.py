import sys
input = sys.stdin.readline

n = input()
coordinate_list = list(map(int, input().split()))
answer_dict = {}

coordinate_set = set(coordinate_list)
coordinate_set = sorted(coordinate_set)

for i in range(len(coordinate_set)):
    answer_dict[coordinate_set[i]] = i

for i in coordinate_list:
    print(answer_dict[i], end=' ')
