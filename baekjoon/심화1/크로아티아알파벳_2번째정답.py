import sys
input = sys.stdin.readline

cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alphabet = str(input().strip())
length = len(alphabet)
count = 0
for i in range(len(alphabet)):
    for j in range(i + 1, len(alphabet) + 1):
        if alphabet[i:j] in cro_list:
            count += 1
            
print(length - count)
