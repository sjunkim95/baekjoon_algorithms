import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    input_num = list(map(int, input().split()))
    if input_num[0] == 1:
        stack.append(int(input_num[1]))
    elif input_num[0] == 2:
        print(-1 if len(stack)==0 else stack.pop())
    elif input_num[0] == 3:
        print(len(stack))
    elif input_num[0] == 4:
        print(1 if len(stack)==0 else 0)
    elif input_num[0] == 5:
        print(-1 if len(stack)==0 else stack[-1])
