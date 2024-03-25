chess_list = [1, 1, 2, 2, 2, 8]
current_list = list(map(int, input().split()))
add_list = []

for i in range(len(chess_list)):
    if chess_list[i] == current_list[i]:
        add_list.append(0)
    elif chess_list[i] != current_list[i]:
        add_list.append(chess_list[i]-current_list[i])
        
print(*add_list)

'''
chess_list = [1, 1, 2, 2, 2, 8]

chess_input = input().split()
chess_left = []

for i in range(len(chess_list)):
    new_chess = chess_list[i] - int(chess_input[i])
    chess_left.append(new_chess)

print(*chess_left)

'''

'''
chess = [1,1,2,2,8] # 기존 체스 개수
A = list(map(int, input().split()))
for i in range(len(chess)):
	print(chess[i] - A[i], end='')
'''
