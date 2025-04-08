print('-----------------------------------------------')
print('-----------------------------------------------')
print('****FUNCION SUMA****')
lista = [1,2,3,4,5]
#Suma de todos los elementos
resultado = sum(lista)

print(f'Resultado de la suma: {resultado}')

#Podemos promorcionar un valor inicial
resultado2 = sum(lista,20)
print(f'Resultado de la suma con valor inicial de 20: {resultado2}')

print('-----------------------------------------------')
print('-----------------------------------------------')
print('****FUNCION NEXT****')
numeros = [10, 20, 30]
it = iter(numeros)  # Creamos un iterador

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
#print(next(it))  # Esto lanzaría StopIteration
print('-----------------------------------------------')

lista2 = (7,8,9,10)
iterador = iter(lista2)
#Obtenemos el proximo elemento del iterador
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
#print(f'Siguiente elemento del iterable: {next(iterador)}') # Esto lanzaría StopIteration