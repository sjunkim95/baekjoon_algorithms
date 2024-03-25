import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
input_list = [i for i in range(n,m+1)]

def prime(num):
    count = 0
    division = num
    while division > 0:
        if num % division == 0:
            count += 1
            division-=1
        elif num % division != 0:
            division-=1
        if division == 1:
            break
    
    if count == 1 and num > 1:
        return num

prime_list = []

for i in range(len(input_list)):
    number = prime(input_list[i])
    if number is not None:
        prime_list.append(number)
if len(prime_list) > 1:
    print(sum(prime_list))
    print(min(prime_list))
if len(prime_list) == 0:
    print("-1")

