def star(fx):
    def wrap(): 
        x=int(input('No. of star you wanna print:'))
        print('*'*x)
        fx()
        print('*'*x)
    return wrap

def hello():
       print('Hello good morning.')  
star(hello)()
    