person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#Exercise 1 
if (('skills' in person)==True):
    skills_list = person['skills']

    middle = len(skills_list)//2 
    print('Middle skill:',skills_list[middle])
else:
    print('Skills not found')

#Exercise 2 

if (('Python' in skills_list)=='True'):
    print('He has the ability ')
else:
    print('He does not have the ability ')
#Execise 3 

if(('JavaScript' in skills_list and 'React' in skills_list)):
    print('He is a front end developer')
elif(('Node' in skills_list and 'Python' in skills_list and 'MongoDB' in skills_list)):
    print('He is a backend developer')
elif(('React' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list)):
    print('He is a fullstack developer')
else:
    print('unknown title')

#Exercise  4 
married = str(input('Is married?'))
live = str(input('Where do you live?'))

if(live =='Finland' and married=='Yes'):
    print('Asabeneh Yetayeh lives in Finland. He is married.')
else:
    print('ok')