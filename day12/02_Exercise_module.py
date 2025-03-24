import random
import string
#Exercise 1 
def list_of_hexa_colors(num):
    hex_co = []
    for _ in range(num):
        random_color = '#' + ''.join(random.choices('0123456789abcdef',k=6))
        hex_co.append(random_color)
    return hex_co
print(list_of_hexa_colors(3))

#Exercise 2 
def list_of_rgb_colors(num):
    lst_rgb = [] 
    for _ in range(num):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        lst_rgb.append(('rgb',red,green,blue))
    return lst_rgb
print(list_of_rgb_colors(4))

#Exercise 3 

def generate_colors(type,num):
    colors = []
    if type == 'hexa':
        for _ in range(num):
            random_color = '#' + ''.join(random.choices('0123456789abcdef',k=6))
            colors.append(random_color)
        return colors
    elif type == 'rgb':
        for _ in range(num):
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            colors.append(('rgb',red,green,blue))
        return colors
    else:
        return 'Invalid color type'
print('Generate Hexa colors:',generate_colors('hexa',3))
print('Generate RGB colors:',generate_colors('rgb',3))
print(generate_colors('tp',5))


  


