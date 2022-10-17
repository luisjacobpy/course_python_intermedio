def run(): # Funcion proncipal
    my_list = [1, 'hello', True, 4.5] # Lista usamos corchetes
    my_dict = {"firstname": "Luis", "lastname": "Hernandez"}

    # Lista de diccionarios
    super_list = [
        {"firstname": "Luis", "lastname": "Hernandez"},
        {"firstname": "Jacobo", "lastname": "Campuzano"},
        {"firstname": "Karina", "lastname": "Monterrubio"},
        {"firstname": "Homero", "lastname": "Simpson"},
        
    ]
    #Diccionario de listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    print('Ciclo for para super list')
    for key, value in super_dict.items(): # Metodo items nos permite recorrer las llaves y valores al mismo tiempo de un diccionario en un ciclo
        #print(key, "-", value)
        print(f'{key}; {value}')

    print('Ciclo for para super dict')
    for i in super_list.items(): # Metodo items nos permite recorrer las llaves y valores al mismo tiempo de un diccionario en un ciclo
        #print(key, "-", value)
        print(f'{key}; {value}')
#Entry point // Lo que hace es iniciar la funcion cuando entramos a nuestro archivo 

if __name__ == '__main__':
    run()

