a = int(input())
temp_list = list(map(int,input().split()))
c = int(input())
count = 0

for i in range(len(temp_list)):
    if c == temp_list[i]:
        count += 1

print(count)
        
