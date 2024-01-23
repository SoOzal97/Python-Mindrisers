# def name(f_name,m_name,l_name,num=3):
#     print(f"Hello {f_name} {m_name} {l_name}\n"*num)

# name(m_name="Bhadhur",f_name="Sujal",l_name="Shrestha",num=2)
 
def sum(*numbers):
    total=0
    for number in numbers:
        total=total+number
    
    print(total)

sum(3,4,5)