import sys

n = int(input())
name_dict = {}

for i in range(n):
    name, state = sys.stdin.readline().split()
    if state == 'enter':
        name_dict[name] = True
    else:
        del name_dict[name]

print("\n".join(sorted(name_dict.keys(), reverse=True)))
