import sys
input = sys.stdin.readline


def binarySearch(array, fdata):
    pos = -1
    start = 0
    end = len(array)-1
    
    while start <= end:
        mid = (start+end)//2
        if fdata == array[mid]:
            return mid
        elif fdata > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1
 
n = int(input())
score_list = list(map(int, input().split()))
score_list.sort()
                  
m = int(input())
find_list = list(map(int, input().split()))

count = 0

for number in find_list:
    findpos = binarySearch(score_list, number)
    if findpos == -1:
        print('0')
    else:
        print('1')
