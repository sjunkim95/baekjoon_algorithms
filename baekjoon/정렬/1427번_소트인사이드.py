import sys
n = sys.stdin.readline()

answer = ''.join(sorted(n))

print(''.join(reversed(answer)))
