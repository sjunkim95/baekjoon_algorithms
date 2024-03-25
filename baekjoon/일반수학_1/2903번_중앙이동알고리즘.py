import sys

n = int(input())

if n > 15 or n < 1:
    sys.exit()
   
print((1+(2**n))**2)


