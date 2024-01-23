# def sum(a, b):
#     return a+b
# print(sum(2,3))

# x= lambda a,b:a+b
# print(x(2,7))
def my_func(n):
    return lambda a:a*n
doubler=my_func(int(input("Number you wanna double:")))
print(doubler(2))
tripler=my_func(int(input("Number you wanna triple:")))
print(tripler(3))