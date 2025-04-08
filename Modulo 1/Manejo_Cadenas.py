#Manejo de cadenas
#dividir una cadena split() (parsing)
print('-----------------------------------------------')

cadena = "Hola Mundo"
palabras = cadena.split() #se generara una lista
palabras2 = cadena.split('M') #(parsing)
print(palabras)
print(palabras2)
print('-----------------------------------------------')

#Buscar con find
posicion = cadena.find('Mundo') #devolvera el valor de 5
print(f'Posicion de la cadena Mundo es: {posicion} ')
print('-----------------------------------------------')

#Reemplazar con replace
nueva_cadena = cadena.replace('Mundo', 'Amigo')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

palabras = "Hola Mundo otra vez Mundo seguimos Mundo"
nueva_cadena2 = palabras.replace('Mundo','Nadia',2)
print(f'Nueva cadena reemplaza varias veces: {nueva_cadena2}')
print('-----------------------------------------------')

#Multiplicacion de cadenas
cadena = 'Hola '
resultado = cadena * 3
print(f'Resulado multiplicacion de cadenas: {resultado}')
print('-----------------------------------------------')

#Limpiar una cadena Strip
cadena = '       Hola Mundo     '
cadena_limpia = cadena.strip()
print(f'Cadena sin limpieza: {cadena}')
print(f'Cadena limpia de espacio al inicio y al final: {cadena_limpia}')

#Limpiar una cadena Strip
cadena3 = '.....Hola Mundo...'
cadena_limpia2 = cadena3.strip('.')
print(f'Cadena sin limpieza: {cadena3}')
print(f'Cadena limpia de caracteres al inicio y al final: {cadena_limpia2}')