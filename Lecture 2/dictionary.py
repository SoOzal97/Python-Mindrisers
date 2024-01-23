person={
    'name': 'sujal',
    'age': '19',
    'qualification':'10+2',
    'family_members':[
        'Mom',
        'Dad',
        'sister'
    ],
    'hobby':('Play games',
             'Watch anime',
             'Coding')
    
}
print('Family members=',person['family_members'],'Hoobies=',person['hobby'])
print(person['family_members'][1])#printing dad from family members variable.
print(person['family_members'][1][-1])#printing the last d from dad.

print('hello my name is {} and I am {} year old. I live with my {}. My hoobies is to {}'.format(person['name'],person['age'],person['family_members'],person['hobby']))
print(f'Hello my name is {person['name']}')