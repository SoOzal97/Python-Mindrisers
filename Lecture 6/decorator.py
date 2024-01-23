# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thankyou for using this function")
#     return mfx
def custom_star(num=0):
    def star(func):
        def wrapper(*args, **kwargs):  
            print('*'*num)
            func() 
        print('*'*num)
        return wrapper
    return star 
def hash(func):
    def wrapper():  
        print('#'*10)
        func()
        print('#'*10)
    return wrapper
@custom_star
def hello(*args, **kwargs):
    print(f"hello world{args[0]}")


 