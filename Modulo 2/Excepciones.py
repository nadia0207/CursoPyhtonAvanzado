print('-----------------------------------------------')
print('-----------------------------------------------')
print('****MANEJO DE EXCEPCIONES****')

def dividir(numerador, denominador):
    try:
        resultado = numerador/denominador
        print(f'Resultado de la division: {resultado}')
    except ZeroDivisionError: 
        print('Error: No se puede dividir entre cero')
    except TypeError:
        print('Error: Los operadores deben ser numericos')

#Ejemplo de uso
dividir(10,2)
dividir(10,0)
dividir(10,'0')

print('\n-------------Otra forma--------------------')
def dividir1(numerador1, denominador1):
    try:
        resultado1 = numerador1/denominador1
        print(f'Resultado de la division: {resultado1}')
    except Exception as e: #de esta manera consideramos todos los errores que se puedan procesar
        print(f'Ocurrio un error: {e}')
    finally: #siempre se va a ejecutar haya o no error
        print('---Terminado de procesar la Excepcion--- \n')

#Ejemplo de uso
dividir1(8,2)
dividir1(8,0)
dividir1(8,'0')