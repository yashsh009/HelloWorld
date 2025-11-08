import math
a=input('Enter the first number: ')
a=float(a)
b=input('enter the second number: ')
b=float(b)
x=input('enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ')
if x=='1':
    print(a + b)
elif x=='2':
    print(a - b)
elif x=='3':
    print(a * b)
elif x=='4':
    print( a / b)
elif x>'4':
    print(x,'is not the options')