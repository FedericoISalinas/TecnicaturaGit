import math

def pitagoras():
    while True:
        print("¿Qué valor desea encontrar?")
        print("1. Hipotenusa.")
        print("2. Cateto a.")
        print("3. Cateto b.")
        print("4. Volver.")
        opcionPitagoras = int(input())
        
        if opcionPitagoras == 1:
            print("Ingrese el valor del cateto a: ", end="")
            cateto1 = float(input())
            print("Ingrese el valor del cateto b: ", end="")
            cateto2 = float(input())
            hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
            print("El resultado de la hipotenusa es: ", hipotenusa)
            input("Presione Enter para continuar...")
            clear_screen()
        elif opcionPitagoras == 2:
            print("Tener en cuenta que el valor de hipotenusa^2 debe ser mayor a cateto b^2, para que el radicando sea mayor a 0")
            print("Ingrese el valor de la hipotenusa: ", end="")
            hipotenusa = float(input())
            print("Ingrese el valor del cateto b: ", end="")
            cateto2 = float(input())
            while hipotenusa**2 <= cateto2**2:
                print("Tener en cuenta que el valor de hipotenusa^2 debe ser mayor a cateto b^2, para que el radicando sea mayor a 0")
                print("Ingrese el valor de la hipotenusa: ", end="")
                hipotenusa = float(input())
                print("Ingrese el valor del cateto b: ", end="")
                cateto2 = float(input())
            cateto1 = math.sqrt(hipotenusa**2 - cateto2**2)
            print("El resultado del cateto a es: ", cateto1)
            input("Presione Enter para continuar...")
            clear_screen()
        elif opcionPitagoras == 3:
            print("Tener en cuenta que el valor de hipotenusa^2 debe ser mayor a cateto a^2, para que el radicando sea mayor a 0")
            print("Ingrese el valor de la hipotenusa: ", end="")
            hipotenusa = float(input())
            print("Ingrese el valor del cateto a: ", end="")
            cateto1 = float(input())
            while hipotenusa**2 <= cateto1**2:
                print("Tener en cuenta que el valor de hipotenusa^2 debe ser mayor a cateto a^2, para que el radicando sea mayor a 0")
                print("Ingrese el valor de la hipotenusa: ", end="")
                hipotenusa = float(input())
                print("Ingrese el valor del cateto a: ", end="")
                cateto1 = float(input())
            cateto2 = math.sqrt(hipotenusa**2 - cateto1**2)
            print("El resultado del cateto b es: ", cateto2)
            input("Presione Enter para continuar...")
            clear_screen()
        elif opcionPitagoras == 4:
            clear_screen()
            break
        else:
            clear_screen()
            print("SELECCIONE UNA OPCIÓN VÁLIDA")

def clear_screen():
    # Este código es para limpiar la pantalla en diferentes sistemas operativos
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

pitagoras()
