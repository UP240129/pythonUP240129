import statistics
#Exercise 1 
def evens_and_odds(r):
    evens=0
    odds=0
    for i in range (0,r+1,+1):
        if(i%2==0):
            evens+=1
        else:
            odds+=1
    return evens,odds
print(evens_and_odds(100))

#Exercise 2 
def factorial(n):
    result=1
    if(n<0):
        return "Factorial is not defined for negative numbers."
    else:
        for i in range(1,n+1):
            result*=i
        return result
print(factorial(5))
print(factorial(0))

#Exercise 3 
def is_empty(value):
    return not bool(value)

print(is_empty([]))
print(is_empty('Hello'))

#Exercise 4 

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calculate_mean(v):
    mean= 0 
    sum =0  #Declarar dentro de la funcion
    for i in (v):
        sum+=i
        mean= sum / (len(v))
    return mean
def calculate_median(v):
    middle=len(v)//2 

    if(len(v)%2==0):
       return v[middle-1:middle+1]
    else:
      return v[middle]
"""def calculate_mode(v):
    return statistics.mode(v)

print(calculate_mode(values))"""

def calculate_mode(v):
    frequency = {}
    for num in v :
        if num  in frequency :
            frequency[num] +=1 
        else:
            frequency[num] = 1
    max_count = max(frequency.values()) 
    modes = [key for key, value in frequency.items() if value == max_count]
    return modes

def calculate_range(v):
    range = max(v) - min(v)
    return range

def calculete_variance(v):
    mean = calculate_mean(v)
    variance = 0 
    for i in (v): 
       variance += (i - mean)**2
    return variance/len(v)


"""def calculate_variance(v):

    mean = calculate_mean(v)

    return sum((x - mean)**2 / len(v))
    
print(calculate_variance(v))"""
    
def calculate_std (v):
    return calculete_variance(v)**0.5


print('Mean:',calculate_mean(values))
print('Median',calculate_median(values))
print('Mode:',calculate_mode(values))
print('Range:',calculate_range(values))
print('Variance:',calculete_variance(values))
print('Standard Deviation:',calculate_std(values))

