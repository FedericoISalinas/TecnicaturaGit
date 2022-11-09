class Persona2:

    def __init__(self, nombre, apellido, edad): # esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostar son los siguientes: {self._nombre} {self._apellido} {self._edad}')
        
    # Metodo Getter
    @property  # decorador
    def nombre(self):
        return self._nombre
    
    # Metodo Setter
    @nombre.setter
    def nombre(self, nombre): 
        self._nombre = nombre
    
     # Metodo Getter
    @property  # decorador
    def apellido(self):
        return self._apellido
    
    # Metodo Setter
    @apellido.setter
    def apellido(self, apellido): 
        self._apellido = apellido
    
     # Metodo Getter
    @property  # decorador
    def edad(self):
        return self._edad
    
    # Metodo Setter
    @edad.setter
    def edad(self, edad): 
        self._edad = edad
    

        
        


persona1 = Persona2 ('Ariel', 'Betancud', 41)
print(persona1.nombre) # Llamamos al metodo getter
persona1.nombre = 'Juan Manuel' # llamamos al metodo setter
print(persona1.nombre) # otra ves con el metodo getter
print(persona1.mostrar_detalle()) # llamamos al metodo mostrar detalle
persona1.apellido = 'De la Mar'
print(persona1.apellido) 
# #Llamamos al metodo mostar detalle atributo red-only seria la edad porque no tiene metodo setter
print(persona1.edad) # metodo getter
# Tarea crear 3 objetos mas, mostrando los metodos getter and setter
    # para modificar y mostrar los cambios

    
persona2 = Persona2('Federico', 'Salinas', 21)
persona2.nombre = 'Federico'
persona2.apellido = 'Salinas'
persona2.edad = 21
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
print(persona2.mostrar_detalle())

persona3 = Persona2('Franco', 'Salinas', 16)
persona3.nombre = 'Franco'
persona3.apellido = 'Salinas'
persona3.edad = 16
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
print(persona3.mostrar_detalle())

persona4 = Persona2('Gonzalo', 'Salinas', 24)
persona4.nombre = 'Gonzalo'
persona4.apellido = 'Salinas'
persona4.edad = 21
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)
print(persona4.mostrar_detalle())



