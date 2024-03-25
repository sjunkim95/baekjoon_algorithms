import sys
input = sys.stdin.readline

String = str(input().strip())
String = String.upper()

max_number = 0
compare = ''
count = 0

for i in String:
    if String.count(i) > max_number:
        max_number = String.count(i)
        compare = i
        count = 1  # 최대 중복 문자가 바뀔 때 count를 초기화
    elif String.count(i) == max_number and i != compare:
        count += 1

print(compare if count == 1 else "?")
