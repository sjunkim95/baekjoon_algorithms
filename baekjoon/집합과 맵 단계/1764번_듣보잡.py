import sys

input = sys.stdin.readline

x, y = map(int,input().split())

name_list1 = [str(input().rstrip()) for i in range(x)]
name_list2 = [str(input().rstrip()) for i in range(y)]

intersection = list(set(name_list1) & set(name_list2))
intersection.sort(reverse=False)
print(len(intersection))
for i in intersection:
    print(i)
