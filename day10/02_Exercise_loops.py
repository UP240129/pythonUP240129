#Exercise 1
n=0
suma=0
while n<=100:
    suma = suma + n
    n+=1
print('The sum of all numbers is :',suma)
#Exericise 2 
print('\n')
k=0
sum=0
sum1=0
while k<=100:
    if(k%2!=0):
        sum= sum +k
    elif(k%2==0):
        sum1 = sum1 +k
    k+=1
print('The sum of all evens is:',sum1,'And the sum of all odds is:',sum)