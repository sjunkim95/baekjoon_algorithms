import sys

N, B = map(int,sys.stdin.readline().split())

strings = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
if B < 2 or B >36:
    sys.exit()
while 0 < N:
    digit = N % B
    result = strings[digit] + result
    N = N // B
	
print(result.upper())
