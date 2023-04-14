class NumerosIgualesException (Exception): #Extiende de la clase
    def init(self, mensaje):
        self.message = mensaje