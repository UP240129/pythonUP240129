print("Calculadora basica")
print("Ingresa numeros del 1 al 4 para detectar el tipo de operacion")
op=int(input("ingresa el tipo de operacion:"))
if (op==1): 
    print('Suma 2 numeros:')
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input('Ingresa el segundo numero:'))
    print (num1 + num2)
elif (op==2) : 
    print('Resta  2 numeros:')
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input('Ingresa el segundo numero:'))
    print (num1 - num2)
elif (op==3) : 
    print('Multiplica 2 numeros:')
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input('Ingresa el segundo numero:'))
    print (num1 * num2)
elif (op==4) : 
    print('Dividide 2 numeros:')
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input('Ingresa el segundo numero:'))
    print (num1 / num2)