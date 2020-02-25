#!/usr/bin/env python3.8

print('Select operation: ')
print('1. Addition')
print('2. Substraction')
print('3. Multiplication')
print('4. Division')
choice = input ('Select choice: 1, 2, 3 or 4: ')
n1= float(input('Enter first number: '))
n2=float(input('Enter second number: '))
if choice == '1':
     print(n1, '+', n2, '=', n1+n2)
elif choice =='2':
    print(n1, '-', n2, '=', n1-n2)
elif choice == '3':
    print(n1, '*', n2, '=', n1*n2)
elif choice == '4':
    print(n1, '/', n2, '=', n1/n2)
else: 
    print('Invalid input')

