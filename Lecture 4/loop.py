# i=0
# while i<=5:
#     if i==3:
#         break
#     print(f'{i}.Hello World')
#     i+=1
fruits=[
    'Apple',#0
    'Banana',#1
    'Mango',#2
    'Papaya',#3
    ['New_list']
    
]
for index,fruit in enumerate(fruits):
    print(index+1,fruit)
    if fruit=='Mango':
        break
for i,x in enumerate('banana'):
    print(i+1,x)
    
# fruits[0]="Chocolate"
# print(fruits)
# print(fruits[4][0][2])
# print('Among them',fruits[2],fruits[1],'are my favourite.') 
# #list are mutable.