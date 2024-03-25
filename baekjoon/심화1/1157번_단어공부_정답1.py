import sys
input = sys.stdin.readline

String = str(input().strip())
String = String.upper()
String_set = list(set(String))

count_list = []

for i in String_set:
    count = String.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    max_index = count_list.index(max(count_list))
    print(String_set[max_index])
