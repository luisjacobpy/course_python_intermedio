""" [Reto: Manejo de excepciones]
Utiliza las palabras clave:
- try
- except
- raise

Para elevear un error si el usuario ingresa un numero negativo en nuestro
programa de divisores.
"""
def run():
    divisors = lambda num: [x for x in range(1, num + 1) if num % x == 0]

    try:
        num = int(input('Ingresa un numero: '))
        if num < 0:
            raise ValueError('Solo ingresa numeros positivos')
        print(divisors(num))
        print("Termino")
    except ValueError:
        print('Solo Ingrese Numeros Positivos :|')
        run() # Se reinicia el programa para que el usuario vuelva a intentar
        

if __name__ == '__main__':
    run()
