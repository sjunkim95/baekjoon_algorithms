n = int(input())
string_list = []
for _ in range(n):
    string = str(input())
    string_list.append(string)

def recursion(s, l, r):
    global cnt
    cnt += 1
    
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in string_list:
    cnt = 0
    print(isPalindrome(i), cnt)
