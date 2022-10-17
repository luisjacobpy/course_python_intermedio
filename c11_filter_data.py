"""
In this project I will filter data in python

"""
# Constante, esta en mayusculas por eso
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

#List comprehensions
def run():
    # Language programming
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # worker representa a cada uno de los diccionarios internos
    # [name] es la llave
    # Creamos un ciclo for
    
    # Organization 
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # Filter  // Hihg order functions whit lambda functions
    """
    Para obtener a todos los adultos (18), se aplica un filter con un lamda,
    posteriormente se usa map para que el resultado no imprima todo el resultado sino 
    unicamente el nombre.

    """
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))    
     
    # Crear una lista de diccionarios
    """
    Unir a worker con una llave más que se agrega al diccionario con pip (|)
    Transformar al diccionario en DATA de nuestro diccioario principal con un nuevo diccioario
    pip | sirve para unir a un diccioario con uno nuevo, con listas lo haciamos con el simbolo (+)
    """
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()
