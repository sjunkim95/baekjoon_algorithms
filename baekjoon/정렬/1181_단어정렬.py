import sys

input = sys.stdin.readline
n = int(input())

string_set = set()

for i in range(n):
    string_set.add(str(input().strip()))

string_set = sorted(string_set, key=lambda x: (len(x), x))

#for i in range(len(string_set)):
#    print(string_set[i])
print('\n'.join(string_set))
