import sys
input = sys.stdin.readline

array = []
for i in range(5):
    String = str(input().strip())
    array.append(String)

max_length = max(len(s) for s in array)

output = ""
for j in range(max_length):
    for i in range(5):
        try:
            output += array[i][j]
        except IndexError:
            continue

print(output)
