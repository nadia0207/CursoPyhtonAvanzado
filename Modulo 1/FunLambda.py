print('***Funciones Lambda***')

#funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2

print(f'el cuadrado de 5 es: {cuadrado(5)}')

#funcion Lambda (anonima)
cuadrado2 = lambda x: x ** 2
print(f'el cuadrado de 4 es: {cuadrado2(4)}')

multiplicacion = lambda x,y : x * y
print(f'La multiplicacion de 3 y 8 es: {multiplicacion(3,8)}')
print("--------------------------------")

