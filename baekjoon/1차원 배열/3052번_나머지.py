num_list=[]
count_set = set()

for i in range(10):
    num_list.append(int(input()))

for i in num_list:
    count_set.add((i % 42))

print(len(count_set))

'''
num_list = []
count_list = []
answer = []

for i in range(10):
    num_list.append(int(input()))

for i in num_list:
    count_list.append(i%42)

for i in count_list:
    if i not in answer:
        answer.append(i)

print(len(answer))
'''
