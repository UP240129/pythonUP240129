import math
import cmath  
#Exercise 1 
def add_two_numbers (num1,num2):
    total = num1 +num2
    return total
print('The result of the sum is:',add_two_numbers(5,5))

#Exercise 2 
def area_of_circle(radio):
    area = radio**2 * math.pi
    return area 
print('The area of circle:',area_of_circle(5))

#Exercise 3 
def add_all_nums(*args):
    if all(isinstance(num,(int,float)) for num in args):
        return sum(args)
    else:
        return "Error: All arguments must be numbers."
print(add_all_nums('The ',1,2,3,4,5,6))
print(add_all_nums(1,2,3,'hello'))

#Exercise 4 

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*(9/5))+ 32
    return fahrenheit
print('Celsius to Fahrenheit:',convert_celsius_to_fahrenheit(32))

#Exercise 5 
def check_season(month):
    if (month=='September' or  month=='Octuber' or month== 'November'):
        return 'Autumn'
    elif(month=='December' or month=='January' or month=='February'):
        return 'Winter'
    elif(month=='March' or month=='April' or month=='May'):
        return 'Spring'
    elif(month=='June' or month=='July' or month=='August'):
        return 'Summer'
print('The season is ',check_season('August'))

#Exercise 6 

def  calculate_slope(x1,x2,y1,y2):
    m=(y2-y1)/(x2-x1)
    return m
print('Slope:',calculate_slope(5,8,10,12))

#Exercise 7 
def solve_quadratic_eqn(a,b,c):
    if(a == 0):

        return "Not a quadratic equation (a must be nonzero)."
    
    discriminat = b**2 - 4*a*c
        #Soluciones reales 
    if discriminat > 0 :
        solution1 = (-b + math.sqrt(discriminat)) / (2 * a)
        solution2 = (-b - math.sqrt(discriminat)) / (2*a)
        return solution1,solution2
        #Solucion unica
    elif discriminat == 0:
        solution1 = (-b / (2*a))
        return solution1
        #Soluciones complejas 
    else:
        solution1 = (-b + cmath.sqrt(discriminat)) / (2 * a)
        solution2 = (-b - cmath.sqrt(discriminat)) / (2*a)
        return solution1,solution2
    
print(solve_quadratic_eqn(1,-3,2)) 

#Exercise 8
def print_list(lst):
    for i in lst:
        print(i)
my_list=[1,2,3,4,5]
print_list(my_list)

#Exercise 9 
def reverse_list(arr):
    reversed_arr=[]
    for i in range(len(arr)-1,-1,-1):
        reversed_arr.append(arr[i])
    return reversed_arr
my_list1=[1,2,3,4,5]
print(reverse_list(my_list1))

#Exercise 10

def capitalize_list_items(cap):
    capitali_list= []
    for i in cap:
        capitali_list.append(i.upper())
    return capitali_list
words= ['hola','adios']
print(capitalize_list_items(words))

#Exercise 11
def add_item(lst,item):
    lst.append(item)
    return lst
print(add_item(my_list,6))   

#Exercise 12

def remove_item(lst,item):
    lst.remove(item)
    return lst
print(remove_item(my_list1,1))

#Exercise 13

def sum_of_numbers(num):
    total = 0 
    for i in range(0,num+1):
        total +=i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Exercise 14

def sum_of_odds(num):
    total = 0 
    for i in range(0,num+1):
        if (i%2!=0):
            total +=i
    return total
print('Sum of the odd numbers:',sum_of_odds(100))
    # return sum(i for i in range(1,num+1,2))
#Exercise 15

def sum_of_evens(num):
    return sum(i for i in range(0, num+1 ,2))
print('Sum of the even numbers:',sum_of_evens(100))