x=input('Enter the smaller number: ')
y=input('Enter the bigger number: ')
x=int(x)
y=int(y)
a=input('Enter how many digits need to find: ')
a=int(a)
if y - x > a-1:
    for n in range(x+1,y):
        print(n)
elif y - x <= a:
    print('Error')