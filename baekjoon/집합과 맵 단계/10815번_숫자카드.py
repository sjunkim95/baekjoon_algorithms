import sys

N_1 = int(sys.stdin.readline())
list_1 = list(map(int,sys.stdin.readline().split()))
N_2 = int(sys.stdin.readline())
list_2 = list(map(int,sys.stdin.readline().split()))
if len(list_1) > N_1 or len(list_2) > N_2:
    sys.exit()

card_dict = dict()

for i in range(N_1):
    card_dict[list_1[i]] = 0

for i in range(len(list_2)):
    if list_2[i] in card_dict:
        print('1', end=' ')
    if list_2[i] not in card_dict:
        print('0', end=' ')
