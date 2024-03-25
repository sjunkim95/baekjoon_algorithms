import sys

input = sys.stdin.readline

String = str(input())
new_list = []

for i in range(len(String)):
    for j in range(1, len(String)):
        temp = String[i:j]
        if temp == '':
            pass
        else:
            new_list.append(String[i:j])

new_list = set(new_list)
print(len(new_list))
