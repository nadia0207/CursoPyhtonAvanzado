print('-----------------------------------------------')
print('-----------------------------------------------')
print('****MANEJO DE EXCEPCIONES****')

print('\n-------------Otra forma--------------------')
#Raise crea excepciones 
def dividir1(numerador1, denominador1):
    try:
        #Revisamos si el denominador es igual a 0
        if denominador1 == 0:
            raise Exception('***El denominador es igual a 0***') #raise lanza una excepcion y ya no continua con la operacion
        
        resultado1 = numerador1/denominador1
        print(f'Resultado de la division: {resultado1}')

    except Exception as e: #de esta manera consideramos todos los errores que se puedan procesar
        print(f'Ocurrio un error: {e}')
    else:#Unicamente se ejecuta cuando no arroje ninguna excepcion
        print(f'No Ocurrio nigún error')       
    finally: #siempre se va a ejecutar haya o no error
        print('---Terminado de procesar la Excepcion--- \n')

#Ejemplo de uso
dividir1(8,2)
dividir1(8,0)
dividir1(8,'0')