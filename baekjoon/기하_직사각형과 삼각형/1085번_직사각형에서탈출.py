import sys
input = sys.stdin.readline

x, y, w, h = map(int,input().split())
x_len = 0
y_len = 0
if x > (w-x):
    x_len = (w-x)
else:
    x_len = x

if y > (h-y):
    y_len = (h-y)
else:
    y_len = y

print(min(x_len,y_len))

'''
print(min(x, y, w-x, h-y)
'''
    
