"""
Desarrollar una función que recibe un numero como parametro y retorna una lista con todos
los divisores
"""

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        #Condicion
        if num % i == 0:
            # Agregar
            divisors.append(i)
    return divisors


# Vamos a pedirle al usuario que introduczca un numero
def run():
    num = int(input('Ingresa un nÃºmero: '))
    print(divisors(num))
    print("TerminÃ³ mi programa")


if __name__ == '__main__':
    run()