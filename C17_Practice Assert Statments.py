"""[Reto]
Utiliza assert statments para evitar que el usuario
ingrese un número negativo en nuestro programa de divisores.
"""

def divisor(num):
    divisors = [i for i in range(1,num+1) if num%i == 0]
    return divisors

def run():
    num = input('Enter a number: ')
    assert num.isnumeric() and int(num)>0, 'Ingresa solo numeros positivos'
    print(divisor(int(num)))
    print('Finish')


if __name__ == '__main__':
    run()