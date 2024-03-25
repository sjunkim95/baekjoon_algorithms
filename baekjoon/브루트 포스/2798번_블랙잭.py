import sys

N, M = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card_list[i] + card_list[j] + card_list[k] > M:
                continue
            else:
                answer = max(answer, card_list[i] + card_list[j] + card_list[k])

print(answer)   

"""
요런 방법도 가능하다

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):  # 중복을 피하기 위해 j+1로 수정
            current_sum = card_list[i] + card_list[j] + card_list[k]
            if current_sum <= M:
                answer = max(answer, current_sum)

"""
