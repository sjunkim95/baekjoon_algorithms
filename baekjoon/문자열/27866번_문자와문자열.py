S = str(input())
i = int(input())

for j in range(1,len(S)+1):
    if i == j:
        print(S[i-1])
