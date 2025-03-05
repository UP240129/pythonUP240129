#Exercise 1 
result = ' '.join(['Tirthy ', 'Days ', 'Of', 'Python'])
print(result)

#Exercise 2 
resultado= ' '.join(['Coding','For', 'All'])
print(resultado)

#Exercise 3
company = 'Coding For All'

#Exercise 4
print(company)

#Exercise 5
print(len(company))

#Exercise 6 


print(company.upper())

#Exercise 7 


print(company.lower())

#Exercise 8 

print(company.capitalize())
print(company.title())
print(company.swapcase())

#Exercise 9 

eliminar_primera = " ".join(company.split()[1:])
print(eliminar_primera)  

#Exercise 10 

print(('Coding' in company))
print(company.find('Coding'))
if (company.index('Coding'))==0 :
    print('La palabra (Coding) se encuentra')

#Exercise 11
companynew= company.replace('Coding', 'Python')
print(company.replace('Coding', 'Python'))

#Exercise 12 
print(companynew.replace('Python For All', ' Python Everyone'))

#Exercise 13
print(company.split())

#Exercise 14

lista = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(lista.split(','))

#Exercise 15

print(company[0])

#Exercise 16
print(company[len(company)-1])

#Exercise 17
print(company[10])

#Exercise 18

company1= 'Python For Everyone'
print(company1[0],company1[7],company1[11])
acronimo = "".join([word[0] for word in company1.split()]).upper()
print(acronimo)

#Exercise 19 
acronimo = "".join([word[0] for word in company.split()]).upper()
print(acronimo)

#Exercise 20
print(company.index('C'))

#Excercise 21 
print(company.index('F'))

#Exercise 22
text = 'Coding For All people'
print(text.rfind('l'))

#Exercise 23
text1= 'You cannot end a sentence with because because because is a conjunction'
print(text1.index('because'))

#Exercise 24
print(text1.rindex('because'))

#Exercise 25
print(text1.replace('because because because',""))

#Exercise 26
print(text1.find('because'))

#Exercise 27
print(text1.replace('because because because',""))

#Exercise 28
print(company.startswith('Coding'))

#Exercise 29 
print(company.endswith('Coding'))

#Exercise 30 
company2= '  Coding For All  '
print(company2.strip())

#Exercise 31
if ("30DaysOfPython".isidentifier()) == True:
    print('30DaysOfPython')  
else:
    print("thirty_days_of_python") 

#Exercise 32
lista2=['Django','Flask','Bottle','Pyramid','Falcon']
print('#, '.join(lista2))

#Exercise 33
print("I am enjoying this challenge.\nI just wonder what is next.")

#Exercise 34
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#Exercise 35
radius = 10 
area = 3.14 * radius **2 
print(f'El area del ciruclo con el radio {radius} es {area} metros cuadrados')

#Exercise 36
a = 8
b = 6 
print(f'{a} + {b} =  {a+b}')
print(f'{a} - {b} =  {a-b}')
print(f'{a} * {b} =  {a*b}')
print(f'{a} / {b} =  {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} =  {a//b}')
print(f'{a} ** {b} =  {a**b}')