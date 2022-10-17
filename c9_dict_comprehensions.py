# Dictionary comprehensions
# Crear los cuadrados de los primeros 100 numeros naturalesn en el diccionario
def run():
#  ------- (Ejemplo de list comprehensions) ---------
    dict_squares = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(dict_squares)

    natural_nums = {i: round(i**0.5, 2)
        for i in range(1, 1001)}
    print(natural_nums)

if __name__ == '__main__':
    run()

