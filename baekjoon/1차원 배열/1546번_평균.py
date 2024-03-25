import sys 

n = int(sys.stdin.readline())

score_list = list(map(int,sys.stdin.readline().split()))
max_score = max(score_list)

for i in range(len(score_list)):
    score_list[i] = score_list[i]/max_score*100
    
answer = sum(score_list)/len(score_list)

print(answer)
