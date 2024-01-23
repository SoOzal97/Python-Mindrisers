x=int(input('Enter your first number:'))
y=int(input('Enter your second number:'))
a=str(input('Enter the arthmetic operation you want to preform: '))
if a=='+':
     print(f'Addition:{x+y}')
     
elif a=='-':
    print(f'Subtraction: {x-y}')
elif a=='*':
    print(f'Multiplication: {x*y}')
elif a=='/':
    print(f'Division: {x/y}')
elif a=='**':
    print(f'Exponentiation: {x**y}')
elif a=='//':
    print(f'Floor Division: {x//y}')
elif a=='%':
    print(f'Modulus:{x%y}')

    a=input('Wanna continue? (yes/no):')
    

    

