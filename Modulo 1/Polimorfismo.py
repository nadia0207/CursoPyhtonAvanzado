#Polimorfismo (se manda a llamar el metodo segun el objeto que se esta ejecutando)

#creacion de la clase Padre Animal
class Animal:
    def hacer_sonido(self):
        print('Puedo hacer sonidos...')

#Creacion de la Clase Hija Chancho
class Chancho(Animal):
    #Esta clase hija no sobreescribe nada solo hereda
    pass

#Creacion de la Clase Hija Perro        
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo Ladrar')

#Creacion de la Clase Hija Gato
class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

#----------------------------------------------------
#Programa principal
#-----------------------------------------------------------
print('***Ejemplo de Polimorfismo***')

print('Clase Padre Animal:')
#definir un objeto de la clase Animal
animal1 = Animal()
#llamando al metodo 
animal1.hacer_sonido()

print('\nClase Hija Chancho:')
#definir un objeto de la clase Chancho
chancho1 = Chancho()
chancho1.hacer_sonido()

print('\nClase Hija Perro:')
#definir un objeto de la clase Perro
perro1 = Perro()
perro1.hacer_sonido()

#definir un objeto de la clase Gato
print('\nClase Hija Gato:')
gato1 = Gato()
gato1.hacer_sonido()