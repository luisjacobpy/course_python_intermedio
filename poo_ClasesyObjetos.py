
# -*- coding: utf-8 -*-
"""
@autor: Luis Jacobo

Sistema de un casino
"""
from random import randint # Nos permite obtener un numero aleatorio de un valor inicial a un valor final.

class Tragamonedas:
    def __init__(self, id, premio):  # Definimos los parametros del contructor
        self.id = id
        self.premio = premio
        self.monedas = 0  # No lo coloco dentro del constructor
        self.jackpots = 0 #Identificar el numero de veces que ha dado el premio


    
    
    # Metodo
    def jugar(self):
        pass



# Instancias / Objetos de la clase
tragamonedas = Tragamonedas(1, 1000.00)
tragamonedas.id
print(tragamonedas.premio)
# Los objetos tienen identidad puedo var la identidad del objeto:
print(id(tragamonedas))  # Esta asociado al lugar de memoria donde esta guardado el objeto

tragamomedas2 = Tragamonedas(2, 200)
