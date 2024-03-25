import sys
input = sys.stdin.readline

n = int(input())

coordinate = list(map(int, input().split()))
coordinate.sort()

print(coordinate)
