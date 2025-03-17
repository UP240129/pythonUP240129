#Exercise 1
print('Con el ciclo while\n')
count = 0
while count <= 10:
    print(count)
    count = count + 1 
print('Con el ciclo for\n')
for i in range(0,11,+1):
    print(i)
    

#Exercise 2
print('Decremento de 0 a 10 con while\n')
count1 = 10 
while count1 >=0 :
    print(count1)
    count1 = count1 - 1
print('Decremento de 0 a 10 con for \n')
for i1 in range(10,-1,-1):
    print(i1)

#Exercise 3
for n in range(0,8,+1):
    print('#'*n)

#Exercise 4
print('\n')
for m in range(0,8):
    print('#  '*8)

#Exercise 5 
print('\n')
for k in range(0,11):
    print(k, 'x', k, '=',(k*k))

#Exercise 6
 
print('\n')
list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in list:
    print(item)

#Exercise 7
print('\n')
for w in range(0,101):
    if (w%2==0):
        print(w)

#Exercise 8
print('\n')
z=0
while z<=100:
    if(z%2!=0):
        print(z)
    z+=1
