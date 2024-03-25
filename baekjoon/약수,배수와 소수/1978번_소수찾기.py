import sys
input = sys.stdin.readline
n = int(input())
prime_list = list(map(int, input().split()))

count_prime = 0

def prime(num):
    global count_prime
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
        count_prime += 1
        return num
    
        


for i in range(len(prime_list)):
    
    prime(prime_list[i])


print(count_prime)
