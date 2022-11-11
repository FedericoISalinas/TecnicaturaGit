from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

print("Creacion de objeto clase Cuadrado".center(50, "_"))

cuadrado1 = Cuadrado(3 , "Azul")
print(f"El ancho del cuadrado es: {cuadrado1.ancho}")
print(f"El alto del cuadrado es: {cuadrado1.alto}")
print(f"Calculo del area del cuadrado: {cuadrado1.calcular_area()}")
print(f"El color del cuadrado es: {cuadrado1.color}")

#MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)
print("Creacion de objeto clase Cuadrado".center(50, "_"))
rectangulo1 = Rectangulo(8, 5, "Rojo")
print(f"El area del rectangulo es: {rectangulo1.area_rectangulo()}")
print(rectangulo1)