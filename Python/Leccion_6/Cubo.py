"""
 Crear una clase cubo con los atributos, ancho, altura y profundidad, con un metodo calcular volumen que 
tendra la formula: volumen = ancho * altura * profundidad que el usuario ingrese los valores

"""
class Cubo:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profunidad = profundidad
        
    def calcular_volumen(self):
        return ancho * altura * profundidad

ancho = int(input("Digite el numero para el ancho del cubo: "))
altura = int(input("Digite el numero para la altura del cubo: "))
profundidad = int(input("Digite el numero para la profunidad del cubo: "))

cubo1 = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")