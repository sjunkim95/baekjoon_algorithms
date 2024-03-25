import sys

input = sys.stdin.readline

N, M = map(int,input().split())

answer = []

def backtrack(start):
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    for i in range(start, N + 1):
        answer.append(i)
        backtrack(i + 1) 
        answer.pop()

backtrack(1)
