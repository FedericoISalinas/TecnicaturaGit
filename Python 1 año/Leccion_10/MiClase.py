class MiClase:
    # Variable de clase, este atributo dara a cada objeto el mismo valor
    variable_clase = "Esta es una variable de clase"
    
    def __init__(self, variable_instancia): # la variable de instancia, da diferentes valores
        self.variable_instancia = variable_instancia
     
    @staticmethod
    def metodo_estatico(): # Metodo estatico, se asocia a la clase
        print(MiClase.variable_clase)
        
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
        
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print("Accedemos a las instancias estaticas con el metodo dinamico metodo_instancia")
        print(self.variable_clase)
        print(self.variable_instancia)
           
print(MiClase.variable_clase, ", llamamos con el objeto MiClase")
print("")
miClase1 = MiClase("Esta es una variable de instancia")
print(miClase1.variable_instancia, ", llamamos con una variable de instancia = miClase1")
print(miClase1.variable_clase, ", llamamos con una variable de instancia = miClase1")
print("")
miClase2 = MiClase("Esta es otra prueba de variable de instancia") 
print(miClase2.variable_clase,", llamamos con otra variable de instancia = miClase2")
print(miClase2.variable_instancia,", llamamos con otra variable de instancia = miClase2")
print("")

MiClase.variable_clase2 = "Valor de variable de clase 2"
print(MiClase.variable_clase2,", usamos otro valor de variable = variable_clase2 ")
print(miClase1.variable_clase2,", usamos otro valor de variable = variable_clase2 ")
print(miClase2.variable_clase2,", usamos otro valor de variable = variable_clase2 ")
print("")

print("Usamos el metodo estatico para llamar al objeto = MiClase.metodo_estatico")
MiClase.metodo_estatico()
print("")

# El contexto ESTATICO trabaja desde la clase 

# El contexto DINAMICO no puede acceder al contexto estatico hasta que no 
# se haya instanciado, una vez que se tenemos un objeto, podemos acceder atraves del objeto
# podemos acceder a un elemento de contexto estatico.

print("Usamos el operador cls") # 
MiClase.metodo_clase()
print("")
# self es un operador que apunta al atributo, para hacer la instancia 
# cls es un operador, pero apunta a la clase en si
print("Creamos un metodo dinamico y accedemos al estatico con = miObjeto1")
miObjeto1 = MiClase("Variable de instancia")
print("Accedemos con mi metodo de instancia (contexto dinamico) a una instancia estatica")
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()
