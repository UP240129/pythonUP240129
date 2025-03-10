import statistics
#Exercise 1 (Level 1) 
list = []
print(list)

#Exercise 2 (Level 1)

list = ['a','b','c','d','e','f']

#Exercise 3 (Level 1)
print('La longitud de la lista es de: ',len(list))

#Exercise 4 (Level 1)

print('El primer objeto es:',list[0])
middle_item = len(list) // 2
print('EL objeto de enmedio es:',middle_item)
print('El ultimo objeto es:',list[-1])

#Exercise 5 ( Level 1)

mixed_data_types = ['Juan Pablo','18','1.80','soltero','Aguascalientes']

#Exercise 6 ( Level 1)

it_companies  =  ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#Exercise 7 ( Level 1)
print(mixed_data_types)
print(it_companies)

#Exercise 8 (Level 1)

print('El numero de compañias es: ',len(it_companies))

#Exercise 9 (Level 1)

print('El primer elemento de la lista es: ',it_companies[0])
middle_item_companie = len(it_companies)//2
print('El elemento de enmedio es:',middle_item_companie)
print('El ultimo valor de la lista es:',it_companies[-1])

#Exercise 10 (Level 1)

it_companies[1] = 'Tesla'
print('Cambio de empresa:',it_companies)

#Exercise 11 (Level 1)
it_companies.append('IT')
print(it_companies)

#Exercise 12 (Level 1)
middle= len(it_companies)//2
it_companies.insert(middle,'IT')
print(it_companies)

#Exercise 13 (Level 1)
it_companies[1] = it_companies[1].upper()
print(it_companies)

#Exercise 14 (Level 1)
print('#, '.join(it_companies))

#Exercise 15 (Level 1)
print('certain ¿esta en la lista?','certain' in it_companies )

#Exercise 16 (Level 1)
it_companies.sort()
print(it_companies)

#Exercise 17 (Level 1)
it_companies.reverse()
print(it_companies)

#Exercise 18 (Level 1)
it_companies1 = it_companies[0:3]
print(it_companies1)

#Exercise 19 (Level 1)
it_companies2 = it_companies[3:]
print(it_companies2)

#Exercise  20 (Level 1)

if ((len(it_companies)) %2!=0):

    print('Los elementos de enmedio en la lista son:',it_companies[middle])

else :
    print('El elemento de enmedio en la lista es:',it_companies[middle + 1: middle - 1])

#Exercise 21 (Level 1)

it_companies.pop(0)
print('Eliminado la primera empresa:',it_companies)

#Exercise 22 (Level 1)
it_companies = ['Amazon', 'Apple', 'Facebook', 'IBM', 'IT', 'Microsoft', 'Oracle', 'TESLA']

mitad_index = len(it_companies) // 2

if len(it_companies) % 2 != 0:
    del it_companies[mitad_index]
else:
    del it_companies[mitad_index - 1: mitad_index + 1]

print("Eliminando la compañia del medio:", it_companies)


#Exercise 23 (Level 1)

it_companies.pop()
print('Eliminando la ultima empresa',it_companies)

#Exercise 24 (Level 1)

it_companies.clear()
print('Eliminando todos los elementos de la lista:',it_companies)

#Exercise 25 (Level 1)
del it_companies

#Exercise 26 (Level 1)

front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node','Express','MongoDB']

##front_end.extend(back_end)
##print(front_end)

#Exercise 27 (Level 1)
full_stack = front_end + back_end
Posicion_redux=full_stack.index('Redux')
full_stack.insert(Posicion_redux+1,'Python')
full_stack.insert(Posicion_redux+2,'SQL')

print(full_stack)

#Exercise 1 (Level 2)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('La minima edad es:',ages[0])
print('La maxima edad es:',ages[-1])

#Exercise 2 (Level 2 )

min_age= ages[0]
max_age= ages[-1]

ages.append(min_age)
ages.append(max_age)

print('La lista actualizada es:',ages)

#Exercise 3 (Level 2)

middle_ages = len(ages) // 2
if (len(ages)%2 != 0 ):
    print('El elemento de enmedio es: ',ages[middle_ages])
else:
    print('Los elementos de enmedio son: ',ages[middle_ages -1: middle_ages+1 ])

#Exercise 4 (Level 2)

promedio = sum(ages) / len(ages)

print('El promedio de los valores de la lista es: ', promedio)

#Exercise 5 (Level 2)

rango = max_age - min_age
print('El rango de edades es: ',rango)

#Exercise 6 (Level 2)

min_diferencia = abs(min_age-promedio)
max_diferencia = abs(max_age-promedio)

print('Minimo - promedio :',min_diferencia)
print('Maximo - promedio :',max_diferencia)
if (min_diferencia>max_diferencia):
    print('Min - el promedio es mayor')
elif (max_diferencia<min_diferencia):
    print(' Max - el promedio es mayor ')
else:
    print('Ambos son iguales')

#Exercise 7 (Level 2)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

middle_contries = len(countries)//2 
if (len(countries)%2 != 0 ):
    print('El elemento de enmedio es: ',countries[middle_contries])
else:
    print('Los elementos de enmedio son: ',countries[middle_contries -1: middle_contries+1 ])

#Exercise 8 (Level 2)

elementos = len(countries)
mid = (elementos//2) + (elementos%2)

primera_parte = countries[:mid]
segunda_parte = countries[mid:]

print(primera_parte)
print(segunda_parte)

#Exercise 9 (Level 2 )

countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

primero , segundo , tercero, * resto = countries2

print('El primer pais es: ',primero)
print('El segundo de los paises es:',segundo)
print('El tercero de los paieses es: ',tercero)
print('El resto de los paises es:', resto)
