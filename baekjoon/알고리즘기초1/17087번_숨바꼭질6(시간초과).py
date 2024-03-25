import sys
input = sys.stdin.readline

N, S = map(int,input().split())

location = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a%b
        return a
answer_list = []
for i in range(len(location)):
    for j in range(i, len(location)):
        distance_1 = location[i] - S
        distance_2 = location[j] - S
        if distance_1 < 0:
            distance_1 = distance_1 * -1
        if distance_2 < 0:
            distance_2 = distance_2 * -1

        answer = gcd(distance_1, distance_2)
        answer_list.append(answer)

print(min(answer_list))
