#Exercise 1 
cal = int(input('Enter your score: '))

if(cal>=90):
    print('Your grade is A')
elif(cal>=70 and cal<=89):
    print('Your grade is B')
elif(cal>=60 and cal<=69):
    print('Your grade is C')
elif(cal>=50 and cal<=59):
    print('Your grade is D')
elif(cal>=0 and cal<=49):
    print('Your grade is F')
else:
    print('I did not enter a valid score')

#Exercise 2 

month = str(input('Enter the month:'))

if (month=='September' or  month=='Octuber' or month== 'November'):
    print('The season is Autumn')
elif(month=='December' or month=='January' or month=='February'):
    print('The season is Winter')
elif(month=='March' or month=='April' or month=='May'):
    print('The season is Spring')
elif(month=='June' or month=='July' or month=='August'):
    print('The season is Summeer')

#Exercise 3
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = str(input('Enter a Fruit:'))

if ((fruit in fruits)==False):
    fruits.append(fruit)
    print('Modified list:',fruits)
else:
    print('That fruit already exist in the list')
