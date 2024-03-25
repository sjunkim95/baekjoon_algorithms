import sys

input = sys.stdin.readline

n = int(input())
answer = 0

for i in range(n):
    if n == i + sum(map(int, str(i))):
        #print(i)
        answer = i
        break

if answer > 0:
    print(answer)
else:
    print('0')
