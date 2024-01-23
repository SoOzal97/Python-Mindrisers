# name="  Hello World"
# print(name)
# print(len(name))
# print(name.lower())
# print(name.strip())
# print(name.split())
# print(name.upper())
fruits=[
    'Apple',#0
    'Banana',#1
    'Mango',#2
    'Papaya'#3
]

vegs=[
    'tomato',
    'potato'
]
fruits.append('kiwi')
print(fruits)
fruits.extend(vegs)
print(fruits)
vegs.insert(1,'cabbage')
print(vegs)
fruits.remove('kiwi')
print(fruits)
vegs.index('tomato')
vegs.sort()
vegs.reverse()
print(vegs)