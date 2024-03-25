import sys
input = sys.stdin.readline

n = int(input())

String_list = [input().strip() for _ in range(n)]

for i in range(len(String_list)):
    stack = 0
    for j in range(len(String_list[i])):
        if String_list[i][j] == '(':
            stack += 1
        elif String_list[i][j] == ')':
            stack -= 1
        if stack == -1:
            print("NO")
            break
    if stack == -1:
        continue
    if stack == 0:
        print("YES")
    else:
        print("NO")

