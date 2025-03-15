#Exercise 1 
empty_dict = {}

#Exercise 2 

dct_masc = {'name':'Kitty','color':'blanco','breed':'Ruffles','legs':'4','age':'1año'}

#Exercise 3

dcy_stu = {'first_name':'Juan Pablo','last_name':'Perez','gender':'Man','age':'18','marital status':'single','skills':['leer','escribir','pensamiento logico'],'country':'Mexico','city':'Aguascalientes','address':'UP240129'}
#Exercise 4 

print(len(dcy_stu))

#Exercise 5
skills = dcy_stu['skills']
print('skills' in dcy_stu)
print(type(skills))

#Exercise 6 
dcy_stu['skills'].append('Inlges')
dcy_stu['skills'].append('Python')

print('Hablidades:',dcy_stu['skills'])

#Exercise 7 
print(dcy_stu.keys())

#Exercise 8 
print(dcy_stu.values())

#Exercise 9 
dcy_stu_tuples = list(dcy_stu.items())

print(dcy_stu_tuples)

#Exercise 10
print(dcy_stu.clear())

#Exercise 11

del dcy_stu


