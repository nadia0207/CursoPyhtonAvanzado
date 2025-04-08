#Creacion de la Clase Padre Animal
class Animal: 
    def comer(self):
        print('Como muchas veces al dia')
    
    def dormir(sel):
        print('Duermo muchas horas')

#Creacion de la Clase Hija Perro
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo Ladrar')
    
    #sobreescribiendo el metodo heredado de la clase padre
    def dormir(sel):
        print('Duermo 15 horas al día')

#Programa principal
print('***Ejemplo de Herencia en Python***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir() #Se llama el metodo sobreecrito en la clase hija
perro1.hacer_sonido()

