try:
    num = int(input('Enter a number: '))
    if num < 0:
        raise Exception('Negative number is not valid')
    print(divisors(num))
    print('[!] Finish...')

except ValueError:
    print('[!] Solo puedes añadir numeeros')
except Exception:
    print('[!] El numero no puede ser negativo')