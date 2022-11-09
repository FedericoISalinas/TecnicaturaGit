class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad): 
        self._edad = edad

    def __str__(self): # Sobreescribir = Override
        return f"Persona: [nombre: {self._nombre}, edad: {self._edad}]"
    
    

class Empleado(Persona): # esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo
            
    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
        
    def __str__(self):
        return f"Empleado: [sueldo: {self._sueldo}] {super().__str__()}"

empleado1 = Empleado ("Ariel", 40, 75000)
print(f'El nombre del empleado es {empleado1.nombre}')
print(f'La edad del empleado es de {empleado1.edad} años')
print(f'El sueldo del empleado es de ${empleado1.sueldo} pesos')

empleado2 = Empleado("Liliana", 38, 70000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado2.nombre = "Natalia"
empleado2.edad = 35
empleado2.sueldo = 75000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)