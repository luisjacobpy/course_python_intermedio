"""
High Order Funtions
-> Filter
-> map
-> reduce

"""


# Tenemos una lista, quiero obtener de todos los numeros que son impares
# my_list = [1, 4, 5, 6, 9, 13, 19, 21]
# odd = [i for i in my_list if i % 2 != 0]
# print(odd)
# Filter
print('En este código se uso \"filter\"')
# Otro ejemplo de Filter
my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 !=0, my_list))
# Inicia lambda
# La funcion filter recibe dos parametros: lambda y un iterable (my_list)
# my_list como iterable
# la funcion filter retorna un iterador <tipo de objeto esspecial>
# lsit <exrterno> como iterador
print(odd)


print('En este código se uso \"list comprehensions\"')
# Función map
# Quiero convertir una lista con los numeros elevados al cuadrado
# Como lo hariamos con list comprehemsions
my_list_n2 = [1, 2, 3, 4, 5]
squares = [i**2 for i in my_list_n2] 
print(squares)

print('En este código se uso \"map\"')

my_list_n2 = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, my_list_n2))
print(squares)

"""
reduce
"""
print('En este código se uso \"for\"')
my_list = [2, 2, 2, 2, 2]
all_multiplied = 1
for i in my_list:
    all_multiplied = all_multiplied * i
print(all_multiplied)


print('En este código se uso \"reduce\"')
"""
Used reduce
I need import a module call reduce

In to lambda: a y b
a = primer elemento de nuestra lista
b = segundo elemento de nuestra lista <es iterativo> 
    
"""
from functools import reduce
my_list = [2, 2, 2, 2, 2]
all_multiplied = reduce(lambda a, b: a * b, my_list)

print(all_multiplied)

