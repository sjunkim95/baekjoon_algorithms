import sys
String = str(input())
if len(String)>15 or len(String)<2:
    sys.exit()

alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 0
for i in String:
    if i in alphabet[0:3]:
        count += 3
    elif i in alphabet[3:6]:
        count += 4
    elif i in alphabet[6:9]:
        count += 5
    elif i in alphabet[9:12]:
        count += 6
    elif i in alphabet[12:15]:
        count += 7
    elif i in alphabet[15:19]:
        count += 8
    elif i in alphabet[19:22]:
        count += 9
    elif i in alphabet[22:26]:
        count += 10

print(count)

'''
String = str(input())
word_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

count = 0
for i in range(len(String)):
    for j in range(len(word_list)):
        if String[i] in word_list[j]:
            count += (j+3)

print(count)

'''
