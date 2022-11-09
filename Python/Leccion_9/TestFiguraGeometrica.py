from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(10, "Azul")
print(f"El ancho del cuadrado es: {cuadrado1.ancho}")
print(f"El alto del cuadrado es: {cuadrado1.alto}")
print(f"Calculo del area del cuadrado: {cuadrado1.calcular_area()}")
print(f"El color del cuadrado es: {cuadrado1.color}")

#MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)
rectangulo1 = Rectangulo(3, 5, "Rojo")
print(f"El area del rectangulo es: {rectangulo1.area_rectangulo()}")
print(rectangulo1)