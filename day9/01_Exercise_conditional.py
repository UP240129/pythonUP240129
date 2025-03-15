#Exercise 1 
age = int(input('Enter your age:'))

if (age>=18):
    print('You are old enough to drive.')
else:
    print('You need',(18-age),'more years to learn to drive')
#Exercise 2 

age1 = int(input('Mi age:'))
age2 = int(input('Your age:'))

dif = age1 -age2 
if (age2>age1 and dif>1):
    print('You are',dif,'years older than me')
elif(age2>age1 and dif==1):
    print('You are 1 year older than me')
elif (age1>age2 and dif==1):
    print('I am 1 year older than you')
else:
     print('I am ',dif,'years older than you.')

#Exercise 3 
n1 = int(input('Enter number one:'))
n2  =int(input('Enter number two:'))

if (n1>n2):
    print(n1,'is greater than',n2)
else:
     print(n2,'is greater than',n1)