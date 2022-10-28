def read():
    numbers = [] # lISTA
    with open("./numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

# Vamos a escribir con el metodo .write  La f representa la conexion que tiene python con nuestros archivos.
# Salto de linea "\n"
def write():
    names = ["Luis", "Kary", "Gugupa", "Jabobo"]
    with open("./archivos/savenames.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)   
            f.write("\n") 



def run():
    write()
# Entry point
if __name__ == "__main__":
    run()


