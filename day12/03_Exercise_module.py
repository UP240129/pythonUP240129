import random
#Exercise 1 
valores = [1,2,3,4,5,6,7,8,9,10]
def shuffle_list(lst):
    r_lst = lst[:]
    random.shuffle(r_lst)
    return r_lst
print('Lista original:',valores)
print('Lista aleatoria:',shuffle_list(valores))

#Exercise 2 

def random_num():
    lst_random_num = set()
    while (len(lst_random_num)<7):
        random_n = random.choice('123456789')
        lst_random_num.add(random_n)
    return list (lst_random_num)
print(random_num())

