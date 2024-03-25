import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
input_list = [i for i in range(n,m+1)]

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return num

prime_list = []

for i in range(len(input_list)):
    if prime(input_list[i]):
        prime_list.append(input_list[i])

if len(prime_list) == 0:
    print("-1")
else:
    print(sum(prime_list))
    print(min(prime_list))
