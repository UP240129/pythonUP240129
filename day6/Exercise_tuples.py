#Exercise 1 (Level 1)
empty_tuple = ()

#Exercise 2 (Level 1)

brothers = ('Jorge','Mateo','Leonel')
sisters = ('Ilse','Mayela','Liz')

print(brothers)
print(sisters)

#Exercise 3 (Level 1)

siblings = brothers + sisters

print(siblings)

#Exercise 4 (Level 1)

print(' I have ',len(siblings),'siblings')

#Exercise 5 (Level 1)

mother = 'Maria'
father = 'Eduardo'

family_members  = siblings+(mother,father)

print('Mi family is:',family_members)

#Exercise 1 (Level 2)

*sibligs,mother,father = family_members
print(sibligs)
print(mother)
print(father)

#Exercise 2 (Level 2)
fruits = ('Manzana','Sandia','Melon')
vegetables = ('Perejil','Lechuga','Cilantro')
animal = ('Mono','Delfin','Leon')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

#Exercise 3 (Level 2)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Exercise 4 (Level 2)
middle = len(food_stuff_tp)//2 

if (len(food_stuff_lt)%2==0):
    print('El elemento de enmedio es:',food_stuff_lt[middle])
else:
    print('Los elementos de enmedio son:',food_stuff_lt[middle -1:middle+1])
#Exercise 5 (Level 2)

print('Los primeros elementos de la lista: ',food_stuff_lt[:3])
print('Los ultimos elementos de la lista son: ',food_stuff_lt[-3:])

#Exercise 6 (Level 2)
del food_stuff_lt

#Exercise 7 (Level 2)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Is Estonia in the nordic countries ','Estonia' in nordic_countries)
print('Is Iceland in the nordic countries ','Iceland' in nordic_countries)
