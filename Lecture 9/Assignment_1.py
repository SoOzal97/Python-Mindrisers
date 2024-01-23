import os
import time


try:
    print('Hello can you provide us with your Info.')
    f_name=str(input("Your First name:"))
    m_name=str(input("Your Middle name:"))
    l_name=str(input("Your last name:"))
    age=(input("Your Age:"))
    f=open('info.txt','w')
    
    f.write(f'{f_name}\n {m_name}\n {l_name}\n {age}')
    
    f.close()
    print("Your file has been created.")
    dlt=str(input("Do you want to delete the created file(yes/no)?\n"))
    if dlt == 'yes':
        print("File will be deleted soon.")
        time.sleep(3)
        os.remove('name.txt')
except Exception as e:
    print(e )
