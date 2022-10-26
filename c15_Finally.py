c15_Finally

""" [finally]
Se usa al final de una estructura, para
1- Cerrar un archivo
2 - Cerrar una conexion a una BDD
3- Liberar recursos externos

"""
try:
    f = open("archivo.txt")
finally:
    f.close()