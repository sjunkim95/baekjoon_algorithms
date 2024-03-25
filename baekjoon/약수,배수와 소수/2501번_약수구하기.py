import sys

x, y = map(int,sys.stdin.readline().split())
count_list = []

for i in range(1, x+1):
    if x%i==0:
        count_list.append(i)
        
#count_list = sorted(count_list)

for i in range(0, len(count_list)):
    if y-1 == i:
        print(count_list[i])

if y>len(count_list):
    print(0)

