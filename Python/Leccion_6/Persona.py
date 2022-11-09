class Persona: # creamos una clase
    # pass # no se procesa nada mas, no tiene contenido
    def  __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # atributos de un objeto dentro de un metodo
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # este atributo esta encapsulado
        self.edad = edad
        self.args = args  
        self.kwargs = kwargs
        
    def mostrar_detalle(self): # self es igual a this
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido}, DNI:  {self._dni}, Edad: {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")
persona1 = Persona("Federico", "Salinas", 43118018, 21) # enviamos argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

persona2 = Persona("Gonzalo", "Salinas", 40123123, 21)
print(f'El nombre del objeto de la clase persona1: {persona1.nombre} {persona1.apellido} y su edad es : {persona1.edad} ')
print(f'El nombre del objeto de la clase persona2: {persona2.nombre} {persona2.apellido} y su edad es : {persona2.edad} ')

#Los objetos no comparten los valores, solo comparten los atributos 

#Modificar los atributos de un objeto
print("")
persona1.nombre = "Franco"
persona1.apellido = "Salinas"
persona1.edad = 16
print(f'El nombre del objeto de la clase persona1: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad}')

#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() # la referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()
# Persona.mostrar_detalle(Persona1) # debemos pasar una referencia para el self sino dara error
# esto es para mejorar el codigo si el dia de mañana nos encontramos una situacion asi

# creamos un atributo una vez ya creada la clase

persona1.telefono = "2604123123" # creamos el atributo telefono a Persona1
print(f"Este es el telefono de {persona1.nombre}: {persona1.telefono}")

# print(Persona2.telefono) el objeto Persona2 no tiene el atributo telefono
persona3 = Persona('Rogelio', 'Romero', 556634456, 22, '26452316213', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
persona4 = Persona('Daniela', 'Blanco', 26913921, 45, '2605412312', 'Calle Sueta', 12525, 'Manzana', 20, 'Casa', 18, Altura=1.83, Peso=60, CFavorito='Negro', Auto='bicicleta', Modelo=2010)
persona4.mostrar_detalle()
# print(persona3._dni) # esto no se debe utilizar ( esta encapsulado) en python, esto dice que lo desconocemos

# persona3.__nombre # esta totalemente encapsulado, no se puede usar
