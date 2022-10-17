palindrome = lambda string: string == string[::-1]
# El string es igual al string al reves?
print(palindrome("ana"))


# Palindrome en funcion.
def palindromo(string): #lo pongo como palindromo para diferenciarlo del lambda
    return string == string[::-1]
print(palindrome("ana"))