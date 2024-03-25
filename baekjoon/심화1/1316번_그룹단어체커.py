n = int(input())

for _ in range(n):
    String = str(input())
    
    for i in range(0, len(String)-1):
        if String[i] == String[i+1]:
            pass
        elif String[i] in String[i+1:]:
            n -= 1
            break
print(n)
