import sys

input = sys.stdin.readline

N, M = map(int,input().split())

answer = []

def backtrack(Start):
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    for i in range(1, N+1):
        answer.append(i) 
        backtrack(Start+i)
        answer.pop() 

backtrack(1)
