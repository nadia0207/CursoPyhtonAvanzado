print('-----------------------------------------------')
print('-----------------------------------------------')
print('**** DECORADORES EN PYHTON****')

def decorador(funcion):
    def envolver(*x, **y ):
        print('Antes de llamar la funcion de saludar')
        resultado = funcion(*x, **y) #llamamos a la funcion
        print('Despues de llamar la funcion saludar')
        return resultado
    return envolver #no poner parentesis () porque solo tenemos que pasar la referencia


@decorador
def saludar (nombre):
    print (f'Hola {nombre}')

saludar('Carlos')
print('-----------------------------------------------')
print('-----------------------------------------------')

def decorador2(func):
    def nueva_funcion(*args, **kwargs):
        print("Llamando a la función con argumentos:", args, kwargs)
        return func(*args, **kwargs)
    return nueva_funcion

@decorador2
def sumar(a, b):
    return a + b

print(sumar(3, 5))
print('-----------------------------------------------')
print('-----------------------------------------------')

#Este ejemplo NO ES DE DECORADORES
def ejemplo(*x, **y):
    print("x =", x)
    print("y =", y)

ejemplo(1, 2, 3, nombre="Carlos", edad=30)
print('-----------------------------------------------')
ejemplo(4,5,6,7, nombre="Nadia", pais="Perú")