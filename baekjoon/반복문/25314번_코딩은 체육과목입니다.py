x=int(input())

ans = 'int'
for i in range(1, x//4+1):
    ans = 'long ' + ans

print(ans)

"""
# 다른 방법

x=int(input())

print("long "*(x//4)+"int")

"""
