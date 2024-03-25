n = int(input())
ans = str(input())
result = 0

if n == len(ans):
    for i in ans:
        i = int(i)
        result += i

print(result)
