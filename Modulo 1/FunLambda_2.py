#******************* map y lambda ********************
#******************************************************
#Supongamos que tienes una lista de números, y quieres obtener una nueva lista con el doble de cada número:
numeros = [1,2,3,4,5]

# Usando map() y lambda para duplicar cada número
dobles = map(lambda x: x * 2 , numeros)

# Convertimos el resultado a lista para verlo
print(list(dobles)) 

print("--------------------------------")
#supamos que tiene una lista de temperaturas en grados Celsius y deseas convertilas a 
#grados Fahrenheit.
celsius = [0,10,50,30]

# Fórmula: F = C * 9/5 + 32
fahrenheit = map(lambda c: c * 9/5 + 32, celsius)

# Convertimos el resultado a lista para verlo
print(list(fahrenheit))

#******************* sorted y lambda ********************
#********************************************************
print("--------------------------------")
lista = [(1,'b'), (3,'a'),(2,'c')]
ordenada = sorted(lista, key= lambda x: x[1])
print(ordenada) 
print("--------------------------------")

#******************* filter y lambda ********************
#********************************************************
#Supongamos que tienes una lista de números, y quieres obtener unicamente los pares de la lista:
numeros2 = [1,2,3,4,5,6]
#realiza el filtro de la lista si el resultado es True agrega a la nueva lista
pares = filter(lambda x: x % 2 == 0, numeros2 )
# Convertimos el resultado a lista para verlo
print(f'Resultado de usar Filter para filtrar numeros pares {list(pares)}')
print("--------------------------------")

#filtrar palabras que tengan más de 5 letras
palabras = ["python", "es", "genial", "y", "muy", "útil"]
largas = filter(lambda palabra: len(palabra) > 5, palabras)
print(list(largas))