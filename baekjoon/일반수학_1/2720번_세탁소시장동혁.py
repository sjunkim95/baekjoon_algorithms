n = int(input())

quarter = 25
dime = 10
nickel = 5
penny = 1

change_list = [int(input()) for i in range(n)]

for i in range(len(change_list)):
    money = change_list[i]
    c_quarter = 0
    c_dime = 0
    c_nickel = 0
    c_penny = 0
    while money>0:
        if money>24:
            c_quarter = int(money/25)
            money -= 25*c_quarter
        elif 9 < money < 25:
            c_dime = int(money/10)
            money -= 10*c_dime
        elif 4 < money < 10:
            c_nickel = int(money/5)
            money -= 5*c_nickel
        if 0 < money < 5:
            c_penny = int(money)
            money -= 1*c_penny

    print(c_quarter, c_dime, c_nickel, c_penny)
