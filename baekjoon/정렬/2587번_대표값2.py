num_list = []
for i in range(5):
    num_list.append(int(input()))

num_list.sort()
print(int(sum(num_list)/len(num_list)))

for i in range(len(num_list)):
    if i==((len(num_list)-1)/2):
        print(num_list[i])
