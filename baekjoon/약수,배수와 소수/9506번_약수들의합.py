import sys

while True:
    number = int(sys.stdin.readline())
    num_list = []
    
    if number == -1:
        break

    for i in range(1, number):
        if (number % i == 0) :
            num_list.append(i)
            
    if sum(num_list) == number:
        print(number, " = ", " + ".join(str(i) for i in num_list), sep="")
    else:
        print(number,"is NOT perfect.")
        
