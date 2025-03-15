#Listas (list): Son ordenadas y mutables, lo que permite modificar, agregar o eliminar elementos. Admiten duplicados y se accede a los elementos mediante índices.
#Tuplas (tuple): Son ordenadas pero inmutables, lo que significa que no pueden modificarse después de su creación. También admiten duplicados y son más rápidas que las listas.
#Conjuntos (set): Son desordenados y no permiten duplicados. Se utilizan para operaciones como la eliminación de elementos repetidos y pruebas de pertenencia eficientes.

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#Exercise 1 (Level 1)

print(len(it_companies))

#Exercise 2 (Level 1)

it_companies.add('Twitter')
print(it_companies)

#Exercise 3 (Level 1)

it_companies.add('Tesla' and 'Huawei')
print(it_companies)

#Exercise 4 (Level 1) 

it_companies.remove('Facebook')
print(it_companies)

#Exercise 5 (Level 1)

it_companies.discard(1)
print(it_companies)

