a = int(input())
temp_list = list(map(int,input().split()))
c = int(input())
count = 0

for i in range(len(temp_list)):
    if c == temp_list[i]:
        count += 1

print(count)
        
"""
# 이런 쉬운 방법도 있다
n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))


# 왜 a 길이 체크는 없지
if len(temp_list.split()) == a :
"""
