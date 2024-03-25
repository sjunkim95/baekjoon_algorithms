import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
array = deque()

for i in range(n):
    command = input().split()
    
    if command[0] == 'push':
        array.append(command[1])
    elif command[0] == 'pop':
        if len(array)==0:
            print('-1')
        else:
            print(array.popleft())
    elif command[0] == 'size':
        print(len(array))
    elif command[0] == 'empty':
        if len(array)==0:
            print('1')
        else:
            print('0') 
    elif command[0] == 'front':
        if len(array)==0:
            print('-1')
        else:
            print(array[0])
    elif command[0] == 'back':
        if len(array)==0:
            print('-1')
        else:
            print(array[-1])


