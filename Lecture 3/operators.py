# a=3
# b=5
# print('addition=',a+b)
# print('Subtraction:',b-a)
# print('Multipication:',b*a)
# print('Division:',b/a)
# print('Modulus:',a%b)
# print(b**a)
# x=5
# x+=5
# print(x)
# y=2
# z=9
# y+=z
# print(y)
# y-=z
# print(y)
# y*=z
# print(y)
# a=8
# a/=2
# print(a)
# a=5
# b='5'
# print(int(b)==a)
# print(type(b))
r=int(input('Enter any number:'))
print(r==5 and r>4) #if one condition is false output is false.
print(r!=6 or r>6) #if one condition is true output is true.
print(not(r!=6 or r>6)) #Prints the exact opposite.
if r>3:
    print(f'{r} is greater than 3.')
elif r==3:
    print(f'{r} equals to 3.')
else:
    print(f'{r} is not greater than 3.')

