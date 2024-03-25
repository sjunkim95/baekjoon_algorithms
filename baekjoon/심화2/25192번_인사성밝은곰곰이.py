import sys

input = sys.stdin.readline

def dance_function(n):
    name_set = set()
    count = 0
    for _ in range(n):
        name = input().strip()
        if name == 'ENTER':
            name_set.clear()
        elif name not in name_set and name != 'ENTER':
            name_set.add(name)
            count += 1
    return count

print(dance_function(int(input().strip())))
