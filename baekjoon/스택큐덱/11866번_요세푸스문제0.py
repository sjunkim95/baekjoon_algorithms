import sys
from collections import deque
input = sys.stdin.readline

x, y = map(int,input().split())

josephus_list = deque([i for i in range(1, x+1)])
answer_list = []

while len(josephus_list)!=0:
    for _ in range(y-1):
        josephus_list.append(josephus_list.popleft())
    answer_list.append(str(josephus_list.popleft()))             

print('<'+', '.join(answer_list)+'>')
