h,m = map(int, input().split())
x = int(input())

h += x//60 
m += x%60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    # 여기서 if문을 한번 더 쓰는 이유 24가 넘었을때에 다시 한번 h값이 변하기에 elif 대신에
    h -= 24

print(h, m)


"""
이런식으로 좀 길어질수
if m >= 60:
    h += 1
    m -= 60
    if h >= 24:
        h -= 24
elif h >= 24:
        h -= 24

"""
