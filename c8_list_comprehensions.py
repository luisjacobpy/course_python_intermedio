# Crear los cuadrados de los primeros 100 numeros naturales
def run():

#  ------- (Ejemplo de list comprehensions) ---------
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)
if __name__ == '__main__':
    run()

# -------( Challenge class)--------
# """
# Crear un list comprehensions, una lista de todos los multiplosde 4 que a la vez también son múltiplos de 6 y de 9, hasta 5 dígitos.

# """
    challenge = [i for i in range (1, 100000) if i % 4 ==0 and i % 6 == 0 and i % 9 == 0]
    print(challenge)