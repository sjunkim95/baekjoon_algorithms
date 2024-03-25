String = str(input())

alphabet ='abcdefghijklmnopqrstuvwxyz'


for i in alphabet:
    if i in String:
        print(String.index(i))
    else:
        print("-1")
