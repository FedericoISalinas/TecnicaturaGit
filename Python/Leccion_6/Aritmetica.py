class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentacion de clase en python
    Vamos a hacer en esta clase algunas operaciones de
    suma, resta, multiplicacion y mas
    """

    def __init__(self, A, B):
        self.A = A
        self.B = B
    def sumar(self):
        return self.A + self.B
    def restar(self):
        return self.A - self.B
    def multiplicar(self):
        return self.A * self.B
    def division(self):
        return self.A / self.B
    

aritmetica1 = Aritmetica (20, 5)
print(aritmetica1.sumar())
print(f"La resta de los numeros es: {aritmetica1.restar()}")
print(f"La multiplicacion de los numeros es: {aritmetica1.multiplicar()}")
print(f"La division de los numeros es: {aritmetica1.division():.2f}")