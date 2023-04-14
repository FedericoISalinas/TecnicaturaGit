from NumerosIgualesExcepiones import NumerosIgualesException
# try: intentar.
# excepcion: error en tiempo de ejecucion.
# Exception : Clase padre. Funciona con Str y Int. Si se ponene mas clases la mimsa tiene que ir al final
# ZeroDivisionError: Clase hija. Funciona con Int. Cuando /0
# TypeError: Clase hija. Str y Int
# ValueError: Clase hija. Letras 
# Finally:  siempre se va a ejecutar, va al final.
# raise: nos permite generar una excepcion


resultado = None
try:
    a = int(input('Digite el primer numero: ' ))
    b = int(input('Digite el segundo numero: ' ))
    if a == b:
        raise NumerosIgualesException('Son numeros iguales')
    resultado = a / b # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {type(e)})')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)})')
except Exception as e:
    print(f'Exception - Ocurrio un error: {type(e)}')
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Ejecucion Finally')

print(f'El resultado es: {resultado}')
print('seguimos...')