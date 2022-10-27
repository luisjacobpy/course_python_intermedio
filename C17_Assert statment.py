"""
[]


"""

def palindrome(string):
        # Afirmo que la longitud del string es mayor a 0, sino corta el programa e imprime el siguiente error
        assert len(string) > 0, "No se puede ingresar una cadena vacia"
        return string == string[::-1]
print(palindrome(""))
