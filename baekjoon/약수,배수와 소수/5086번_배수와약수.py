import sys

while True:
    x, y = map(int,sys.stdin.readline().split())
    if x<y and y%x == 0:
        print('factor')
    elif x>y and x%y == 0:
        print('multiple')
    elif x==0 and y==0:
        break
    else:
        print('neither')

    
