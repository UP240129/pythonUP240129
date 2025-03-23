import keyword
from data_countries import languages_dict
from collections import Counter
#Exercise 1 
n = int(input('Enter a number:'))
def is_prime(num):
    if num % 2 !=0:
        return 'Is prime'
    else:
        return 'Not is prime'
print(is_prime(n))

#Exercise 2 
list = [1,2,3,4,5,6,4]
def unique(lst):
    frequency={}
    for i in lst:
        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i] = 1 
    if (max(frequency.values())==1):
        return 'Todos los elementos son unicos'
    else:
        return 'Hay elementos repetidos'
print(unique(list))

#Exercise 3 

ast= [1,3,4]
def check_same_data(lst):
    if not lst :
        return 'No hay elementos'
    pt = type(lst[0])
    for i in lst:
        if type(i) != pt: 
           return 'Hay diferentes tipos de datos'
    return 'Todos los datos son del mismo tipo'
print(check_same_data(ast))

#Exercise 4 
#Solo puede contener letras, numeros y guiones bajos
#No puede ser una palabra reservada
#No puede empezar con un numero 

def is_valid_variable(name):
    if not name.isidentifier():
        return 'No es valido'
    if name in keyword.kwlist:
        return 'No es valido'
    return 'Es un nombre valido para una variable'
print(is_valid_variable('hola'))
print(is_valid_variable('def'))
print(is_valid_variable('5num'))
print(is_valid_variable('hola/i'))

#Exercise 5 
def most_popular_languages(dict):
    all_languages = [lang for country in dict for lang in country['languages']] 
    language_cout = Counter(all_languages)
    top10 = language_cout.most_common(10)
    return top10
print(most_popular_languages(languages_dict))

#Exercise 6 

def most_populated_countries(dict):
    most_populated=[]
    top10_countries = sorted(dict, key=lambda x: x["population"], reverse=True)[:10]
    print('The countries with most population:')
    for country in top10_countries:
        most_populated.append(f"{country['name']} - {country['population']}")
    return most_populated
print(most_populated_countries(languages_dict))