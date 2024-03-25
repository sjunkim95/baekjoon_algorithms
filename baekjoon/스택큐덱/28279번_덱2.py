import sys
from collections import deque

input = sys.stdin.readline

array = deque()

n = int(input())

for i in range(n):
    command = input().split()
    
    if command[0] == '1':
        array.appendleft(command[1])
    elif command[0] == '2':
        array.append(command[1])
    elif command[0] == '3':
        if len(array) == 0:
            print('-1')
        else:
            print(array.popleft())
    elif command[0] == '4':
        if len(array) == 0:
            print('-1')
        else:
            print(array.pop())
    elif command[0] == '5':
        print(len(array))
    elif command[0] == '6':
        if len(array) == 0:
            print('1')
        else:
            print('0')
    elif command[0] == '7':
        if len(array) == 0:
            print('-1')
        else:
            print(array[0])
    elif command[0] == '8':
        if len(array) == 0:
            print('-1')
        else:
            print(array[-1])
    
