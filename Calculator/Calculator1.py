def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def product(a,b):
    return a*b
def division(a,b):
    return a/b

while True:
    
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
    n=int(input("Choose the operation you wanna do(1/2/3/4):"))
    if n==1:
        print(sum(a,b))
    elif n==2:
        print(sub(a,b))
    elif n==3:
        print(product(a,b))
    elif n==4:
        print(division(a,b))
    c=str(input('DO you want to continue?(yes/no):'))
    if c=='no':
        break
