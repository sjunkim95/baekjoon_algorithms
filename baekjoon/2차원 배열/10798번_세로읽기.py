import sys
input = sys.stdin.readline

array = []
for i in range(5):
    String = str(input().strip())
    array.append(String)

# 가장 긴 문자열의 길이 찾기
max_length = max(len(s) for s in array)

# 출력
j = 0
while True:
    for i in range(5):
        try:
            # 현재 인덱스에 문자가 있다면 출력
            print(array[i][j], end="")
        except IndexError:
            # 인덱스 에러가 발생하면 무시하고 다음 루프로 진행
            continue

    # 가장 긴 문자열의 길이만큼 출력했으면 루프 종료
    if j == max_length - 1:
        break

    j += 1
