H,M = map(int, input().split())

if M<=44 and H>=1:
    print(H-1, M+15)
elif M>=45:
    print(H, M-45)
else:
    print(23, M+15) # 왜냐면 H의 길이를 봐야지 0을 입력했다면 else지
    
