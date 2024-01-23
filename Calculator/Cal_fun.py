
def add():
    sum=num1+num2
    print(f"The sum of two numbers are:{sum}")
def sub():
    diff=num1-num2
    print(f"The difference of two numbers are:{sum}")
    
def multipication():
    product=num1*num2
    print(f"The product of two numbers are:{sum}")
def division():
    division=num1/num2
    print(f"The division of two numbers are:{sum}")
num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
print("1.Add")
print("2.Subtract")
print("3.Multipy")
print("4.Division")
a=str(input('Enter the arthmetic operation you want to preform(1/2/3/4): '))
if a=='1':
     add()   
elif a=='2':
    sub()
elif a=='3':
    multipication()
elif a=='4':
   division()
b=str(input("Do you wanna continue(yes/no)?"))


