import sys
input = sys.stdin.readline

def binarySearch(array, fdata):
    start = 0
    end = len(array) - 1
    
    while start <= end:
        mid = (start + end) // 2
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

count_dict = {}
for number in find_list:
    count = 0
    findpos = binarySearch(score_list, number)
    while findpos != -1:
        findpos = binarySearch(score_list, number)
        if findpos != -1:
            count += 1
            del(score_list[findpos])
    count_dict[number] = (count)

#print(count_dict)
for i in count_dict.values():
    print(i, end=" ")
"""
answer_array = []
for number in find_list:
    count = 0
    findpos = binarySearch(score_list, number)
    while findpos != -1:
        findpos = binarySearch(score_list, number)
        if findpos != -1:
            count += 1
            del(score_list[findpos])
    answer_array.append(count)
            
print(*answer_array)
"""
