import os
import time


try:
    print('Hello can you provide us with your name.')
    f_name=str(input("Your First name:"))
    m_name=str(input("Your Middle name:"))
    l_name=str(input("Your last name:"))
    f=open('name.txt','w')
    
    f.write(f'{f_name}\n {m_name}\n {l_name}')
    # text=f.readlines()
    # print(text[-1])
    f.close()
    print("File will be deleted soon.")
    time.sleep(3)
    #f=open('hello.txt', 'w')
    # print(f.write())
except Exception as e:
    print(e )
