import sys
input = sys.stdin.readline

second_list = []
for _ in range(9):
    second_list.append(list(map(int, input().split())))


max_number = 0
row = 0
col = 0

for i in range(len(second_list)):
    for j in range(len(second_list)):
        if second_list[i][j] >= max_number:
            max_number = second_list[i][j]
            row = i+1
            col = j+1

print(max_number)
print(row, col)

'''        
max_list = []
for i in range(len(second_list)):
    max_list.append(max(second_list[i]))
find_number = max(max_list)
'''
'''
if second_list[i][j] == find_number:
            row = i+1
            col = j+1

'''
